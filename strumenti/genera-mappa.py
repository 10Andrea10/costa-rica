"""Rigenera il file unico HTML dai dati. Nessun pacchetto Python richiesto.
Leaflet 1.9.4 è incorporato dal file in mappe/leaflet-1.9.4.js e CSS.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / 'mappe/attivita.json').read_text())
leaflet_js = (ROOT / 'mappe/leaflet-1.9.4.js').read_text()
leaflet_css = (ROOT / 'mappe/leaflet-1.9.4.css').read_text()
leaflet_license = (ROOT / 'mappe/LEAFLET-LICENSE.txt').read_text()
payload = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
template = '''<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Costa Rica · giorno per giorno</title>
<style>__LEAFLET_CSS__</style>
<style>
:root{--ink:#16332d;--muted:#52675f;--paper:#f3f5ee;--card:#fff;--line:#d8e1d5;--accent:#126759;--soft:#e7efe7}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}header{background:#123d33;color:#fff;padding:24px max(18px,calc((100vw - 1160px)/2));}header small{color:#c3ddcc;letter-spacing:.12em;text-transform:uppercase;font-size:11px}h1{font-size:29px;line-height:1.1;margin:7px 0 9px;font-weight:650}header p{margin:0;font-size:14px;color:#e5efe6}.tabs{display:flex;gap:7px;overflow-x:auto;padding:13px max(16px,calc((100vw - 1160px)/2));background:#fff;position:sticky;top:0;z-index:1100;border-bottom:1px solid var(--line)}button,.button{font:inherit;cursor:pointer;border:1px solid var(--line);border-radius:12px;background:#fff;color:var(--ink);padding:10px 15px;text-decoration:none;display:inline-block}button:focus-visible,a:focus-visible{outline:3px solid #dc9d33;outline-offset:3px}.tabs button{white-space:nowrap;font-size:14px;min-height:44px}.tabs button[aria-selected=true]{background:var(--ink);color:#fff;border-color:var(--ink)}main{max-width:1200px;margin:auto;padding:20px;display:grid;grid-template-columns:minmax(0,1fr) minmax(340px,.9fr);gap:24px}.eyebrow{color:var(--muted);font-size:12px;letter-spacing:.09em;font-weight:650}h2{font-size:27px;line-height:1.15;margin:7px 0 10px}.badge{display:inline-block;border:1px solid var(--line);background:var(--soft);border-radius:6px;padding:4px 9px;font-size:12px;font-weight:650}.intro{font-size:15px;margin:13px 0}.budget{border-left:4px solid var(--accent);padding:12px 14px;background:#e7eee1;font-size:14px;border-radius:0 10px 10px 0;margin:18px 0}.stop{display:grid;grid-template-columns:34px 1fr;gap:12px;background:var(--card);padding:16px;border:1px solid var(--line);border-radius:15px;margin:12px 0}.num{border-radius:50%;height:30px;width:30px;display:grid;place-items:center;background:var(--accent);color:#fff;font-weight:650;font-size:14px}.stop time{font-size:12px;letter-spacing:.035em;font-weight:650;color:var(--muted)}.stop h3{font-size:17px;line-height:1.25;margin:5px 0 8px}.stop p{font-size:14px;margin:0 0 10px;color:var(--muted)}.stop a{font-size:14px;color:var(--accent);font-weight:650;text-underline-offset:3px}.stop .label{font-size:11px;text-transform:uppercase;margin-left:7px;color:var(--muted)}.map-panel{position:sticky;top:82px;align-self:start;background:#fff;border-radius:18px;padding:16px;border:1px solid var(--line)}.map-head{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:10px}.map-head h3{font-size:16px;margin:0}.map-buttons{display:flex;gap:6px}.map-buttons button{font-size:12px;padding:8px 11px}.map-buttons button[aria-pressed=true]{background:var(--ink);color:white}.map-box{height:400px;position:relative;border-radius:12px;overflow:hidden;background:#e7eee1}#schematic,#streetmap{width:100%;height:100%;display:block}#streetmap{display:none}.fine{font-size:12px;color:var(--muted);margin:12px 0 0}.note{font-size:14px;border-top:1px solid var(--line);padding-top:14px;margin-top:18px}.pin{background:transparent;border:none}.pin span{display:grid;place-items:center;width:30px;height:30px;border:2px solid #fff;border-radius:50%;background:var(--accent);color:#fff;box-shadow:0 2px 6px #0004;font-size:13px;font-weight:bold}.map-message{margin:8px 0 0;font-size:12px;color:var(--muted)}footer{max-width:1160px;margin:0 auto 30px;padding:0 20px;color:var(--muted);font-size:12px}footer a{color:var(--accent)}details{margin-top:12px}summary{cursor:pointer;font-size:13px}.all-days{display:none}
@media(max-width:760px){header{padding:20px 18px}h1{font-size:26px}main{grid-template-columns:1fr;padding:16px;gap:18px}.map-panel{position:static;grid-row:1}.map-box{height:280px}h2{font-size:24px}.map-panel{padding:12px}.tabs{padding:10px 14px}.stop{padding:14px}.budget{margin:14px 0}}
@media print{header{background:white;color:#16332d}header p,header small{color:#52675f}.tabs,.map-buttons{display:none}main{display:block}.map-panel{position:static;break-inside:avoid}.map-box{height:300px}#streetmap{display:none!important}#schematic{display:block!important}.stop{break-inside:avoid}a{color:#126759}}
</style></head><body>
<header><small>5-12 novembre 2026 · due persone · auto</small><h1>Costa Rica, giorno per giorno</h1><p>Una tappa alla volta. Aggiornamento 5 novembre · orari Costa Rica.</p></header>
<nav class="tabs" aria-label="Scegli giornata" role="tablist" id="tabs"></nav>
<main><section id="day" aria-live="polite"></section><aside class="map-panel" aria-label="Mappa della giornata">
<div class="map-head"><h3>Le tappe sulla mappa</h3><div class="map-buttons"><button id="offline" aria-pressed="true">Schema offline</button><button id="online" aria-pressed="false">Strade online</button></div></div>
<div class="map-box"><svg id="schematic" viewBox="0 0 520 400" role="img" aria-label="Schema geografico delle tappe"></svg><div id="streetmap" aria-label="Mappa OpenStreetMap"></div></div>
<p class="fine">Pin indicativi. Le linee indicano l'ordine delle visite, <strong>non il percorso stradale</strong>. Per guidare usa i link Google Maps cercando il nome dell'ingresso.</p>
<p id="map-message" class="map-message">Lo schema funziona senza rete. La base stradale richiede internet.</p>
<details><summary>Aprire dal telefono / Telegram</summary><p class="fine">Scarica il documento HTML e aprilo nel browser. Se l'anteprima non esegue le interazioni, usa il PDF condiviso insieme. Nessuna posizione GPS richiesta. <a href="costa-rica-giorno-per-giorno.pdf">Apri il PDF offline</a>.</p></details>
</aside></main>
<footer>Bozza iterativa, nessun nuovo biglietto prenotato. Il giro gratuito del 5 è scelto; 6-7 e relativi costi sono da riconfermare; 8-11 restano aperti. Confermati auto, orario obiettivo aeroporto, alloggio 5-8 e volo 12 alle 18:20.<br>
Fonti: <a href="https://www.sinac.go.cr/ES/servlin/Paginas/default.aspx">SINAC</a> · <a href="https://www.visitcostarica.com/sites/default/files/2024-10/INGLES_FORTUNA.pdf">Visit Costa Rica</a> · <a href="https://misticopark.com/">Mistico</a> · <a href="https://kayakparadiseandtours.com/">Kayak Paradise</a> · <a href="https://www.munisarchi.go.cr/articulo/17/carreta%2C-simbolo-de-trabajo">Sarchí</a> · <a href="https://imn.ac.cr/es/web/imn/reporte-pronostico-regional">IMN</a>.<br>Leaflet 1.9.4 incorporato; mappa stradale © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>. Nessuna mappa stradale scaricata per uso offline. Ingressi a pagamento solo dopo conferma del costo.</footer>
<noscript><div style="padding:24px">Per i pulsanti dei giorni serve JavaScript. Apri il PDF per leggere tutte le giornate senza JavaScript.</div></noscript>
<script id="trip-data" type="application/json">__DATA__</script>
<script>__LEAFLET_JS__</script>
<script id="trip-app">
const trip=JSON.parse(document.getElementById('trip-data').textContent);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const navUrl=q=>'https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(q);
const labels={confirmed:'Confermato',booked:'Alloggio confermato',proposed:'Proposta',alternative:'Alternativa',optional:'Extra',open:'Da scegliere',idea:'Idea'};
let current=trip.days[0], mode='offline', map=null, markers=null, tileLayer=null;
function points(day){return day.stops.map((s,i)=>({...s,n:i+1})).filter(s=>s.coord);}
function drawSchema(day){
 const pts=points(day), svg=document.getElementById('schematic');
 if(!pts.length){svg.innerHTML='<text x="30" y="180" fill="#52675f" font-size="18">Nessuna rotta ancora scelta</text>';return;}
 let xs=pts.map(p=>p.coord[1]),ys=pts.map(p=>p.coord[0]);let xmin=Math.min(...xs),xmax=Math.max(...xs),ymin=Math.min(...ys),ymax=Math.max(...ys);
 let dx=Math.max(xmax-xmin,.035),dy=Math.max(ymax-ymin,.035),cx=(xmin+xmax)/2,cy=(ymin+ymax)/2;
 dx=Math.max(dx,dy*1.15);dy=Math.max(dy,dx/1.6);xmin=cx-dx*.7;xmax=cx+dx*.7;ymin=cy-dy*.7;ymax=cy+dy*.7;
 const xy=p=>[52+(p.coord[1]-xmin)/(xmax-xmin)*416,340-(p.coord[0]-ymin)/(ymax-ymin)*280];
 let h='<rect width="520" height="400" fill="#edf2e8"/><text x="18" y="25" fill="#52675f" font-size="12">N ↑ · posizioni indicative · non navigazione</text>';
 for(let i=0;i<5;i++){let x=52+i*104,y=60+i*70;h+=`<path d="M ${x} 60 V 340 M 52 ${y} H 468" stroke="#d7e0d2" fill="none"/><text x="${x}" y="365" text-anchor="middle" fill="#52675f" font-size="10">${(xmin+i*(xmax-xmin)/4).toFixed(2)}°</text><text x="47" y="${y+4}" text-anchor="end" fill="#52675f" font-size="10">${(ymax-i*(ymax-ymin)/4).toFixed(2)}°</text>`;}
 if(pts.length>1 && day.id!=='idee')h+=`<polyline points="${pts.map(p=>xy(p).join(',')).join(' ')}" fill="none" stroke="${day.color}" stroke-width="2.5" stroke-dasharray="6 6" opacity=".65"/>`;
 const clusters=[];for(const p of pts){const [x,y]=xy(p);const group=clusters.find(g=>{const [a,b]=xy(g[0]);return Math.hypot(x-a,y-b)<28;});if(group)group.push(p);else clusters.push([p]);}
 for(const group of clusters){const p=group[0];let [x,y]=xy(p),num=group.map(t=>t.n).join('/'),anchor=x>320?'end':'start',tx=x>320?x-19:x+19;const names=[...new Set(group.map(t=>t.short))];const label=names.length>2?'Zona La Fortuna':names.join(' / ');
 h+=`<g><circle cx="${x}" cy="${y}" r="15" fill="${day.color}" stroke="#fff" stroke-width="2"/><text x="${x}" y="${y+4}" text-anchor="middle" fill="#fff" font-size="${num.length>3?9:12}" font-weight="600">${num}</text><text x="${tx}" y="${y-17}" text-anchor="${anchor}" fill="#16332d" font-size="13" font-weight="600">${esc(label)}</text></g>`;}
 svg.innerHTML=h;
}
function drawStreet(day){
 if(typeof L==='undefined'){document.getElementById('map-message').textContent='Mappa stradale non disponibile: usa lo schema offline o Google Maps.';return;}
 if(!map){map=L.map('streetmap',{scrollWheelZoom:false}).setView([10.2,-84.4],8);tileLayer=L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18,attribution:'© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>'}).addTo(map);tileLayer.on('tileerror',()=>{document.getElementById('map-message').textContent='Base stradale non caricata: passa a Schema offline. I pin restano indicativi.';});markers=L.layerGroup().addTo(map);}
 markers.clearLayers();const pts=points(day);for(const p of pts){const icon=L.divIcon({className:'pin',html:`<span style="background:${day.color}">${p.n}</span>`,iconSize:[30,30],iconAnchor:[15,15]});L.marker(p.coord,{icon}).addTo(markers).bindPopup(`<b>${esc(p.name)}</b><br>${esc(p.time)}<br><a href="${navUrl(p.query)}" target="_blank" rel="noopener">Cerca ingresso in Google Maps</a>`);}
 if(pts.length>1&&day.id!=='idee')L.polyline(pts.map(p=>p.coord),{color:day.color,weight:2,dashArray:'6 7'}).addTo(markers);
 map.invalidateSize();if(pts.length>1)map.fitBounds(L.latLngBounds(pts.map(p=>p.coord)).pad(.25));else if(pts.length)map.setView(pts[0].coord,day.id==='8-11'?9:12);
}
function showDay(id){
 current=trip.days.find(d=>d.id===id)||trip.days[0];document.documentElement.style.setProperty('--accent',current.color);
 for(const b of document.querySelectorAll('[role=tab]')){const selected=b.dataset.day===current.id;b.setAttribute('aria-selected',String(selected));b.tabIndex=selected?0:-1;}
 document.getElementById('day').innerHTML=`<div class="eyebrow">${esc(current.date)}</div><h2>${esc(current.title)}</h2><span class="badge">${esc(current.status)}</span><p class="intro">${esc(current.intro)}</p><div class="budget"><strong>Budget attività</strong><br>${esc(current.budget)}</div>${current.stops.map((s,i)=>`<article class="stop"><div class="num">${i+1}</div><div><time>${esc(s.time)}</time><span class="label">${esc(labels[s.kind])}</span><h3>${esc(s.name)}</h3><p>${esc(s.detail)}</p>${s.query?`<a href="${navUrl(s.query)}" target="_blank" rel="noopener">Apri in Google Maps ↗</a>`:''}</div></article>`).join('')}<p class="note">${esc(current.note)}</p>`;
 drawSchema(current);if(mode==='online')drawStreet(current);
}
document.getElementById('tabs').innerHTML=trip.days.map(d=>`<button role="tab" data-day="${d.id}" aria-selected="false">${esc(d.tab)}</button>`).join('');
for(const b of document.querySelectorAll('[role=tab]'))b.addEventListener('click',()=>showDay(b.dataset.day));
document.getElementById('offline').addEventListener('click',()=>{mode='offline';document.getElementById('schematic').style.display='block';document.getElementById('streetmap').style.display='none';document.getElementById('offline').setAttribute('aria-pressed','true');document.getElementById('online').setAttribute('aria-pressed','false');});
document.getElementById('online').addEventListener('click',()=>{mode='online';document.getElementById('schematic').style.display='none';document.getElementById('streetmap').style.display='block';document.getElementById('online').setAttribute('aria-pressed','true');document.getElementById('offline').setAttribute('aria-pressed','false');drawStreet(current);});
showDay('5');
</script></body></html>'''
out = template.replace('__DATA__', payload).replace('__LEAFLET_CSS__', leaflet_css).replace('__LEAFLET_JS__', leaflet_js)
out = out.replace('<script>'+leaflet_js, '<!-- Leaflet 1.9.4 license:\n'+leaflet_license+'\n-->\n<script>'+leaflet_js, 1)
(ROOT / 'mappe/costa-rica-giorno-per-giorno.html').write_text(out)
print('HTML generato, byte:', len(out.encode()))
