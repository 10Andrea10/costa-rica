// Framework di sistema, nessun pacchetto installato.
// Eseguire dalla radice del progetto:
// CLANG_MODULE_CACHE_PATH=/private/tmp/costa-rica-clang-cache swiftc -module-cache-path /private/tmp/costa-rica-swift-cache strumenti/genera-pdf.swift -o /private/tmp/costa-rica-pdf
// /private/tmp/costa-rica-pdf
import Foundation
import CoreGraphics
import CoreText
import PDFKit
import AppKit
import ImageIO
import UniformTypeIdentifiers

struct Stop: Decodable { let time: String; let name: String; let short: String; let detail: String; let query: String?; let coord: [Double]?; let kind: String }
struct Day: Decodable { let id: String; let tab: String; let date: String; let title: String; let status: String; let color: String; let intro: String; let budget: String; let note: String; let stops: [Stop] }
struct Trip: Decodable { let title: String; let updated: String; let timezone: String; let subtitle: String; let days: [Day] }
let root = URL(fileURLWithPath: FileManager.default.currentDirectoryPath)
let trip = try JSONDecoder().decode(Trip.self, from: Data(contentsOf: root.appendingPathComponent("mappe/attivita.json")))
let out = root.appendingPathComponent("mappe/costa-rica-giorno-per-giorno.pdf")
let qa = URL(fileURLWithPath: "/private/tmp/costa-rica-pdf-verifica", isDirectory: true)
try FileManager.default.createDirectory(at: qa, withIntermediateDirectories: true)
let W: CGFloat = 480, H: CGFloat = 1080, M: CGFloat = 27, content: CGFloat = 426
func color(_ h: String) -> CGColor { let t = h.replacingOccurrences(of: "#", with: ""); let n = UInt64(t, radix: 16) ?? 0; return CGColor(red: CGFloat((n >> 16) & 255)/255, green: CGFloat((n >> 8) & 255)/255, blue: CGFloat(n & 255)/255, alpha: 1) }
let ink = color("16332d"), muted = color("52675f"), paper = color("f3f5ee"), line = color("d8e1d5")
let white = CGColor(gray: 1, alpha: 1)
let fontName = "Helvetica"
func attributed(_ s: String, _ size: CGFloat, _ c: CGColor, _ bold: Bool = false) -> NSAttributedString {
 let name = bold ? "Helvetica-Bold" : fontName
 let font = CTFontCreateWithName(name as CFString, size, nil)
 var ls: CGFloat = 3
 let para = withUnsafePointer(to: &ls) { p in CTParagraphStyleCreate([CTParagraphStyleSetting(spec: .lineSpacingAdjustment, valueSize: MemoryLayout<CGFloat>.size, value: p)], 1) }
 return NSAttributedString(string: s, attributes: [NSAttributedString.Key(kCTFontAttributeName as String): font, NSAttributedString.Key(kCTForegroundColorAttributeName as String): c, NSAttributedString.Key(kCTParagraphStyleAttributeName as String): para])
}
func height(_ s: String, _ size: CGFloat, _ width: CGFloat, _ bold: Bool = false) -> CGFloat {
 let f = CTFramesetterCreateWithAttributedString(attributed(s,size,ink,bold)); let z = CTFramesetterSuggestFrameSizeWithConstraints(f, CFRange(location:0,length:0), nil, CGSize(width:width,height:10000), nil)
 return ceil(z.height) + 3
}
@discardableResult func text(_ ctx: CGContext, _ s: String, _ x: CGFloat, _ top: CGFloat, _ width: CGFloat, _ size: CGFloat, _ c: CGColor = ink, _ bold: Bool = false) -> CGFloat {
 let h = height(s,size,width,bold), f = CTFramesetterCreateWithAttributedString(attributed(s,size,c,bold)); let path = CGPath(rect: CGRect(x:x,y:H-top-h,width:width,height:h+2), transform:nil)
 ctx.textMatrix = .identity; CTFrameDraw(CTFramesetterCreateFrame(f,CFRange(location:0,length:0),path,nil),ctx); return h
}
func rect(_ ctx: CGContext, _ x: CGFloat, _ top: CGFloat, _ w: CGFloat, _ h: CGFloat, _ fill: CGColor, radius: CGFloat = 10) {
 ctx.setFillColor(fill); ctx.addPath(CGPath(roundedRect: CGRect(x:x,y:H-top-h,width:w,height:h),cornerWidth:radius,cornerHeight:radius,transform:nil));ctx.fillPath()
}
func stroke(_ ctx: CGContext, _ ax: CGFloat,_ at: CGFloat,_ bx: CGFloat,_ bt: CGFloat,_ c: CGColor,_ width: CGFloat = 1) {ctx.setStrokeColor(c);ctx.setLineWidth(width);ctx.move(to:CGPoint(x:ax,y:H-at));ctx.addLine(to:CGPoint(x:bx,y:H-bt));ctx.strokePath()}
func link(_ ctx: CGContext,_ query: String,_ top: CGFloat,_ x: CGFloat = 76) {
 var parts = URLComponents(string:"https://www.google.com/maps/search/")!;parts.queryItems=[URLQueryItem(name:"api",value:"1"),URLQueryItem(name:"query",value:query)]
 ctx.setURL(parts.url! as CFURL,for:CGRect(x:x,y:H-top-19,width:content-70,height:20))
}
func map(_ ctx: CGContext, _ day: Day,_ top: CGFloat,_ h: CGFloat) {
 rect(ctx,M,top,content,h,color("e7eee1"),radius:12)
 _=text(ctx,"SCHEMA GEOGRAFICO  ·  N ↑",M+13,top+10,content-26,10,muted,true)
 let pts=day.stops.enumerated().compactMap{ i,s -> (Int, Stop)? in s.coord == nil ? nil : (i+1,s)}
 guard !pts.isEmpty else { _=text(ctx,"Nessuna rotta ancora scelta",M+20,top+70,content-40,15,muted);return }
 let lons=pts.map{$0.1.coord![1]},lats=pts.map{$0.1.coord![0]}
 var dx=max(lons.max()!-lons.min()!,0.035),dy=max(lats.max()!-lats.min()!,0.035)
 let cx=(lons.max()!+lons.min()!)/2,cy=(lats.max()!+lats.min()!)/2
 dx=max(dx,dy*1.2);dy=max(dy,dx/2)
 let xmin=cx-dx*0.68,xmax=cx+dx*0.68,ymin=cy-dy*0.68,ymax=cy+dy*0.68
 let left=M+48,right=M+content-38,up=top+45,down=top+h-29
 func pos(_ s: Stop)->CGPoint { CGPoint(x:left+CGFloat((s.coord![1]-xmin)/(xmax-xmin))*(right-left),y:down-CGFloat((s.coord![0]-ymin)/(ymax-ymin))*(down-up)) }
 for i in 0...4 {let x=left+CGFloat(i)*(right-left)/4, y=up+CGFloat(i)*(down-up)/4;stroke(ctx,x,up,x,down,line,0.5);stroke(ctx,left,y,right,y,line,0.5)}
 let accent=color(day.color)
 if pts.count>1 && day.id != "idee" {
  ctx.saveGState();ctx.setLineDash(phase:0,lengths:[4,5]);for i in 1..<pts.count {let a=pos(pts[i-1].1),b=pos(pts[i].1);stroke(ctx,a.x,a.y,b.x,b.y,accent,1.5)};ctx.restoreGState()
 }
 var clusters:[[(Int,Stop)]]=[]
 for entry in pts {
  let p=pos(entry.1)
  if let k=clusters.firstIndex(where:{let q=pos($0[0].1);return hypot(p.x-q.x,p.y-q.y)<24}) {clusters[k].append(entry)} else {clusters.append([entry])}
 }
 for group in clusters {let s=group[0].1;let p=pos(s);let nums=group.map{String($0.0)}.joined(separator:"/")
  ctx.setFillColor(accent);ctx.fillEllipse(in:CGRect(x:p.x-11,y:H-p.y-11,width:22,height:22))
  let font:CGFloat=nums.count>3 ? 7.5 : 10
  let numberLine=CTLineCreateWithAttributedString(attributed(nums,font,white,true))
  let nw=CTLineGetTypographicBounds(numberLine,nil,nil,nil)
  ctx.textMatrix = .identity;ctx.textPosition=CGPoint(x:p.x-CGFloat(nw)/2,y:H-p.y-font*0.35);CTLineDraw(numberLine,ctx)
  let unique=Array(Set(group.map{$0.1.short})).sorted()
  let label=unique.count>2 ? "Zona La Fortuna" : unique.joined(separator:" / ")
  let x=p.x>W*0.63 ? p.x-132 : p.x+15
  _=text(ctx,label,max(M+4,x),p.y-25,125,10,ink,true)
 }
 _=text(ctx,"Pin indicativi. Linee = ordine visite, non strade.",M+13,top+h-19,content-26,9,muted)
}
var media = CGRect(x:0,y:0,width:W,height:H)
guard let ctx = CGContext(out as CFURL,mediaBox:&media,[kCGPDFContextTitle:"Costa Rica in auto - giorno per giorno",kCGPDFContextAuthor:"Pianificazione con l'utente"] as CFDictionary) else {fatalError("PDF non creato")}
let kindLabels=["confirmed":"CONFERMATO","booked":"ALLOGGIO CONFERMATO","proposed":"PROPOSTA","optional":"EXTRA","alternative":"ALTERNATIVA","open":"DA SCEGLIERE","idea":"IDEA"]
for (page,day) in trip.days.enumerated() {
 ctx.beginPDFPage(nil);ctx.setFillColor(paper);ctx.fill(media)
 rect(ctx,0,0,W,7,color(day.color),radius:0)
 var y:CGFloat=22
 y += text(ctx,day.date,M,y,content,10,muted,true)+4
 y += text(ctx,day.title,M,y,content,23,ink,true)+5
 y += text(ctx,day.status,M,y,content,11,color(day.color),true)+8
 y += text(ctx,day.intro,M,y,content,11.5,muted)+12
 let budgetH=height(day.budget,11.5,content-26)+35
 let sizes=day.stops.map{s -> CGFloat in 14+height(s.time,10,content-64,true)+height(s.name,13,content-64,true)+height(s.detail,11,content-64)+8+(s.query == nil ? 0:21)}
 let noteH=height(day.note,10.5,content)+12
 let available=H-y-budgetH-sizes.reduce(0,+)-CGFloat(sizes.count)*9-noteH-73
 let mapH=min(195,max(120,available))
 map(ctx,day,y,mapH);y+=mapH+12
 rect(ctx,M,y,content,budgetH,color("e2eada"))
 _=text(ctx,"BUDGET ATTIVITÀ",M+13,y+9,content-26,9.5,color(day.color),true)
 _=text(ctx,day.budget,M+13,y+26,content-26,11.5,ink);y+=budgetH+12
 for (index,s) in day.stops.enumerated() {
  let h=sizes[index];rect(ctx,M,y,content,h,white)
  ctx.setFillColor(color(day.color));ctx.fillEllipse(in:CGRect(x:M+11,y:H-y-35,width:25,height:25))
  _=text(ctx,String(index+1),M+19,y+16,20,10,white,true)
  var yy=y+10
  yy+=text(ctx,s.time,76,yy,content-64,10,muted,true)
  yy+=text(ctx,s.name,76,yy,content-64,13,ink,true)+2
  yy+=text(ctx,s.detail,76,yy,content-64,11,muted)
  if let q=s.query {yy+=2;_=text(ctx,"Apri in Google Maps  >",76,yy,content-64,10.5,color(day.color),true);link(ctx,q,yy)}
  y+=h+9
 }
 y+=3;y+=text(ctx,day.note,M,y,content,10.5,muted)
 if y>H-38 {fatalError("Pagina \(day.id) oltre margine: \(y)")}
 stroke(ctx,M,H-29,W-M,H-29,line,0.7)
 _=text(ctx,"Costa Rica · bozza 5 novembre 2026 · nessun nuovo acquisto",M,H-23,content-40,8.5,muted)
 _=text(ctx,"\(page+1)/\(trip.days.count)",W-M-30,H-23,30,8.5,muted)
 ctx.endPDFPage()
}
ctx.closePDF()
guard let doc=PDFDocument(url:out),doc.pageCount==trip.days.count else {fatalError("PDF non leggibile")}
var counts:[String]=[]
for i in 0..<doc.pageCount {
 guard let page=doc.page(at:i) else {fatalError("Pagina mancante")}
 let box=page.bounds(for:.mediaBox), scale:CGFloat=1.5
 guard let bitmap=CGContext(data:nil,width:Int(box.width*scale),height:Int(box.height*scale),bitsPerComponent:8,bytesPerRow:0,space:CGColorSpaceCreateDeviceRGB(),bitmapInfo:CGImageAlphaInfo.premultipliedLast.rawValue) else {fatalError("Render non creato")}
 bitmap.scaleBy(x:scale,y:scale);bitmap.setFillColor(white);bitmap.fill(box);page.draw(with:.mediaBox,to:bitmap)
 let target=qa.appendingPathComponent(String(format:"pagina-%02d.png",i+1))
 guard let img=bitmap.makeImage(),let dest=CGImageDestinationCreateWithURL(target as CFURL,UTType.png.identifier as CFString,1,nil) else{fatalError("PNG non creato")}
 CGImageDestinationAddImage(dest,img,nil);guard CGImageDestinationFinalize(dest) else{fatalError("PNG non scritto")}
 let extracted=page.string ?? ""
 guard extracted.contains(trip.days[i].title),extracted.count>200 else {fatalError("Testo PDF incompleto pagina \(i+1)")}
 counts.append("\(i+1): \(extracted.count) caratteri")
}
print("PDF: \(out.path)\nPagine: \(doc.pageCount)\nPNG verifica: \(qa.path)\n"+counts.joined(separator:"\n"))
