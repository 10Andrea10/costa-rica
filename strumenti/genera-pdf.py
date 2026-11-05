"""PDF portabile da attivita.json. Dipendenze fissate in requirements.txt."""
from io import BytesIO
from pathlib import Path
from urllib.parse import urlencode
from xml.sax.saxutils import escape
import json
import math

import reportlab
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parent.parent
W, H, M = 480, 1080, 27
CONTENT = W - 2 * M
INK, MUTED, PAPER = '#16332d', '#52675f', '#f3f5ee'
FONT_DIR = Path(reportlab.__file__).resolve().parent / 'fonts'
for name, filename in [('Vera', 'Vera.ttf'), ('Vera-Bold', 'VeraBd.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
LABELS = {'confirmed': 'CONFERMATO', 'booked': 'ALLOGGIO CONFERMATO',
          'proposed': 'PROPOSTA', 'optional': 'EXTRA', 'alternative': 'ALTERNATIVA',
          'open': 'DA SCEGLIERE', 'idea': 'IDEA'}


def paragraph(value, size=11, color=MUTED, bold=False, markup=False):
    value = str(value).replace('→', ' > ').replace('↑', 'Nord').replace('–', '-').replace('—', '-')
    style = ParagraphStyle('text', fontName='Vera-Bold' if bold else 'Vera',
                           fontSize=size, leading=size * 1.35, textColor=HexColor(color))
    return Paragraph(value if markup else escape(str(value)), style)


def height(value, width, size=11, bold=False):
    return paragraph(value, size, bold=bold).wrap(width, H * 100)[1]


def text(c, value, x, top, width, size=11, color=MUTED, bold=False, markup=False):
    p = paragraph(value, size, color, bold, markup)
    _, h = p.wrap(width, H * 100)
    p.drawOn(c, x, H - top - h)
    return h


def box(c, x, top, width, h, color, radius=10):
    c.setFillColor(HexColor(color))
    c.roundRect(x, H - top - h, width, h, radius, stroke=0, fill=1)


def line(c, x1, y1, x2, y2, color='#d8e1d5', width=.5):
    c.setStrokeColor(HexColor(color))
    c.setLineWidth(width)
    c.line(x1, H - y1, x2, H - y2)


def draw_map(c, day, top, h):
    box(c, M, top, CONTENT, h, '#e7eee1', 12)
    text(c, 'SCHEMA GEOGRAFICO · NORD', M + 13, top + 10, CONTENT - 26, 10, bold=True)
    pts = [(i + 1, s) for i, s in enumerate(day['stops']) if s.get('coord')]
    if not pts:
        text(c, 'Nessuna rotta ancora scelta', M + 20, top + 65, CONTENT - 40, 14)
        return
    lats = [s['coord'][0] for _, s in pts]
    lons = [s['coord'][1] for _, s in pts]
    dx, dy = max(max(lons) - min(lons), .035), max(max(lats) - min(lats), .035)
    cx, cy = (max(lons) + min(lons)) / 2, (max(lats) + min(lats)) / 2
    dx = max(dx, dy * 1.2)
    dy = max(dy, dx / 2)
    left, right, up, down = M + 48, W - M - 38, top + 47, top + h - 30

    def pos(s):
        lat, lon = s['coord']
        return (left + (lon - cx + dx * .68) / (dx * 1.36) * (right - left),
                down - (lat - cy + dy * .68) / (dy * 1.36) * (down - up))

    for i in range(5):
        x, y = left + i * (right - left) / 4, up + i * (down - up) / 4
        line(c, x, up, x, down)
        line(c, left, y, right, y)
    if day['id'] != 'idee':
        c.saveState()
        c.setDash(4, 5)
        for (_, a), (_, b) in zip(pts, pts[1:]):
            line(c, *pos(a), *pos(b), day['color'], 1.5)
        c.restoreState()
    groups = []
    for entry in pts:
        x, y = pos(entry[1])
        group = next((g for g in groups if math.dist((x, y), pos(g[0][1])) < 24), None)
        if group is None:
            groups.append([entry])
        else:
            group.append(entry)
    for group in groups:
        x, y = pos(group[0][1])
        nums = '/'.join(str(i) for i, _ in group)
        c.setFillColor(HexColor(day['color']))
        c.circle(x, H - y, 11, stroke=0, fill=1)
        c.setFillColor(white)
        size = 7.5 if len(nums) > 3 else 10
        c.setFont('Vera-Bold', size)
        c.drawCentredString(x, H - y - size * .35, nums)
        names = list(dict.fromkeys(s['short'] for _, s in group))
        label = ' / '.join(names)
        label_x = max(M + 4, x - 132 if x > W * .63 else x + 15)
        text(c, label, label_x, y - 30, min(130, W - M - label_x), 9, INK, True)
    text(c, 'Pin indicativi. Linee = ordine visite, non strade.', M + 13,
         top + h - 19, CONTENT - 26, 8.5)


def generate():
    trip = json.loads((ROOT / 'mappe/attivita.json').read_text())
    stream = BytesIO()
    c = canvas.Canvas(stream, pagesize=(W, H), invariant=1)
    c.setTitle('Costa Rica in auto - giorno per giorno')
    c.setAuthor('Pianificazione con l’utente')
    page_count = 0

    def start(day, continuation=False):
        nonlocal page_count
        page_count += 1
        box(c, 0, 0, W, H, PAPER, 0)
        box(c, 0, 0, W, 7, day['color'], 0)
        y = 22
        y += text(c, day['date'], M, y, CONTENT, 10, bold=True) + 4
        title = day['title'] + (' (segue)' if continuation else '')
        y += text(c, title, M, y, CONTENT, 23, INK, True) + 5
        y += text(c, day['status'], M, y, CONTENT, 10, day['color'], True) + 9
        return y

    def finish():
        line(c, M, H - 29, W - M, H - 29)
        text(c, 'Costa Rica · ' + trip['updated'] + ' · nessun nuovo acquisto',
             M, H - 23, CONTENT - 45, 7.5)
        text(c, str(page_count), W - M - 25, H - 23, 25, 8)
        c.showPage()

    for day in trip['days']:
        y = start(day)
        y += text(c, day['intro'], M, y, CONTENT, 11) + 12
        draw_map(c, day, y, 160)
        y += 172
        bh = height(day['budget'], CONTENT - 26, 11) + 35
        box(c, M, y, CONTENT, bh, '#e2eada')
        text(c, 'BUDGET ATTIVITÀ', M + 13, y + 9, CONTENT - 26, 9, day['color'], True)
        text(c, day['budget'], M + 13, y + 26, CONTENT - 26, 11, INK)
        y += bh + 12
        for i, stop in enumerate(day['stops'], 1):
            width = CONTENT - 64
            label = stop['time'] + ' · ' + LABELS[stop['kind']]
            h = (height(label, width, 9, True) + height(stop['name'], width, 12, True)
                 + height(stop['detail'], width, 10.5) + 27 + (19 if stop.get('query') else 0))
            if h > H - 210:
                raise ValueError(f'Tappa troppo lunga: {stop["name"]}; accorciare il testo.')
            if y + h > H - 65:
                finish()
                y = start(day, True) + 8
            box(c, M, y, CONTENT, h, '#ffffff')
            c.setFillColor(HexColor(day['color']))
            c.circle(M + 23, H - y - 24, 12, stroke=0, fill=1)
            c.setFont('Vera-Bold', 10)
            c.setFillColor(white)
            c.drawCentredString(M + 23, H - y - 27, str(i))
            yy = y + 10
            yy += text(c, label, 76, yy, width, 9, bold=True) + 3
            yy += text(c, stop['name'], 76, yy, width, 12, INK, True) + 4
            yy += text(c, stop['detail'], 76, yy, width, 10.5)
            if stop.get('query'):
                yy += 4
                url = 'https://www.google.com/maps/search/?' + urlencode({'api': 1, 'query': stop['query']})
                text(c, '<link href="' + escape(url, {'"': '&quot;'}) + '">Apri in Google Maps &gt;</link>',
                     76, yy, width, 10, day['color'], True, markup=True)
            y += h + 9
        nh = height(day['note'], CONTENT, 10.5)
        if y + nh > H - 45:
            finish()
            y = start(day, True) + 8
        text(c, day['note'], M, y + 3, CONTENT, 10.5)
        finish()
    c.save()
    out = ROOT / 'mappe/costa-rica-giorno-per-giorno.pdf'
    temp = out.with_suffix('.pdf.tmp')
    temp.write_bytes(stream.getvalue())
    temp.replace(out)
    print(f'PDF generato: {out} ({page_count} pagine)')


if __name__ == '__main__':
    generate()
