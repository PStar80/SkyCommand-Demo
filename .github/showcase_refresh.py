#!/usr/bin/env python3
"""One-time documentation asset refresh using the existing approved artwork."""
from __future__ import annotations
import hashlib, html, json, sys
from pathlib import Path
import xml.etree.ElementTree as ET
SVG='http://www.w3.org/2000/svg'
ET.register_namespace('',SVG)
ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
CYAN,WHITE,MUTED='#25D6FF','#F0F7FC','#A4BDCF'
DEFS='''<defs>
<linearGradient id="surface" x2="1" y2="1"><stop stop-color="#06111C"/><stop offset=".55" stop-color="#07131F"/><stop offset="1" stop-color="#020A12"/></linearGradient>
<linearGradient id="metal" x2="1" y2="1"><stop stop-color="#D8E7EE"/><stop offset=".10" stop-color="#3C596D"/><stop offset=".26" stop-color="#9DB5C4"/><stop offset=".42" stop-color="#1F3547"/><stop offset=".57" stop-color="#6B96B1"/><stop offset=".72" stop-color="#E3F4FF"/><stop offset=".84" stop-color="#365569"/><stop offset="1" stop-color="#91ACBF"/></linearGradient>
<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#40BCFF" stroke-opacity=".055"/></pattern>
<linearGradient id="shade"><stop stop-color="#020B14" stop-opacity=".93"/><stop offset=".36" stop-color="#020B14" stop-opacity=".72"/><stop offset=".67" stop-color="#020B14" stop-opacity=".08"/><stop offset="1" stop-color="#020B14" stop-opacity=".02"/></linearGradient>
<linearGradient id="bottomShade" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#020B14" stop-opacity="0"/><stop offset=".6" stop-color="#020B14" stop-opacity=".05"/><stop offset="1" stop-color="#020B14" stop-opacity=".85"/></linearGradient>
<radialGradient id="halo"><stop stop-color="#6BE8FF"/><stop offset="1" stop-color="#25D6FF" stop-opacity="0"/></radialGradient>
<marker id="arrow" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="5" markerHeight="5" orient="auto"><path d="M1 1L7 4L1 7Z" fill="#25D6FF"/></marker>
</defs>'''
STYLE='''<style>
.sweep{animation:sweep 26s linear infinite}.spark{animation:sweep 26s linear infinite}
.stream{animation:data 6s linear infinite}.halo{opacity:.16;animation:breathe 7s ease-in-out infinite}
.ring{animation:data 18s linear infinite}.dust{animation:drift 11s ease-in-out infinite}
@keyframes sweep{to{stroke-dashoffset:-100}}@keyframes data{to{stroke-dashoffset:-100}}
@keyframes breathe{0%,100%{opacity:.10}50%{opacity:.26}}
@keyframes drift{0%,100%{transform:translateY(0);opacity:.16}50%{transform:translateY(-5px);opacity:.5}}
@media(prefers-reduced-motion:reduce){.sweep,.spark,.stream,.halo,.ring,.dust{animation:none!important}}
</style>'''
def text(x,y,value,size=20,color=WHITE,weight=400,anchor='start',extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{html.escape(value)}</text>'
def rect(x,y,w,h,fill='#071A29',stroke='#26718A',extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" {extra}/>'
def frame(x,y,w,h,background=True):
    out=rect(x+2,y+2,w-4,h-4,'url(#surface)' if background else 'none','url(#metal)','stroke-width="2"')
    out+=rect(x+7,y+7,w-14,h-14,'url(#grid)' if background else 'none','#163349')
    d=f'M{x+2} {y+2}H{x+w-2}V{y+h-2}H{x+2}Z'
    out+=f'<path d="{d}" fill="none" stroke="{CYAN}" stroke-width="1.5" opacity=".5" pathLength="100" stroke-dasharray="6 94" class="sweep"/>'
    out+=f'<path d="{d}" fill="none" stroke="#E6FAFF" stroke-width="1.5" opacity=".65" pathLength="100" stroke-dasharray="1.2 98.8" class="spark"/>'
    for xx,yy,dx,dy in ((x+9,y+9,1,1),(x+w-9,y+9,-1,1),(x+9,y+h-9,1,-1),(x+w-9,y+h-9,-1,-1)):
        out+=f'<path d="M{xx+12*dx} {yy}H{xx}V{yy+12*dy}" fill="none" stroke="#A9C9DD" opacity=".65"/>'
    return out

def doc(w,h,title,desc,body):
    return f'<svg xmlns="{SVG}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc" font-family="Segoe UI,Arial,sans-serif">\n<title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(desc)}</desc>\n{DEFS}\n{STYLE}\n{body}\n</svg>\n'

def hero(art,mobile=False):
    w,h=(480,410) if mobile else (960,320)
    scale=(h-16)/173
    tx=(w*.70-301*scale) if mobile else 8
    body=f'<defs><clipPath id="artClip"><rect x="8" y="8" width="{w-16}" height="{h-16}"/></clipPath></defs>'
    body+=rect(0,0,w,h,'#04101B','none')
    body+=f'<g clip-path="url(#artClip)"><g transform="translate({tx:.5f} 8) scale({scale:.8f})">'
    body+=f'<image width="649" height="173" href="{art}"/>'
    body+='<ellipse cx="301" cy="57" rx="73" ry="53" fill="url(#halo)" class="halo"/>'
    paths=['M82 78C136 69 129 112 180 100S224 96 257 113','M166 45C215 43 196 94 246 104L273 117','M347 115C417 115 386 55 428 44','M371 111C429 86 441 122 477 84S524 80 548 68','M415 125C451 123 485 142 514 132']
    for i,d in enumerate(paths):
        body+=f'<path d="{d}" fill="none" stroke="#D8FAFF" stroke-width="1.5" stroke-linecap="round" pathLength="100" stroke-dasharray="3 97" opacity=".8" class="stream" style="animation-delay:-{i*1.35}s"/>'
    body+='<ellipse cx="304" cy="124" rx="103" ry="13" fill="none" stroke="#81EFFF" stroke-width="1.1" pathLength="100" stroke-dasharray="11 89" opacity=".65" class="ring"/>'
    for i,(cx,cy) in enumerate(((181,26),(393,25),(486,145),(212,140),(466,28))):
        body+=f'<circle cx="{cx}" cy="{cy}" r="1.2" fill="#8CEAFF" opacity=".25" class="dust" style="animation-delay:-{i*2}s"/>'
    body+='</g></g>'
    body+=rect(8,8,w-16,h-16,'url(#shade)','none')+rect(8,8,w-16,h-16,'url(#bottomShade)','none')
    body+=rect(8,8,w-16,h-16,'url(#grid)','none')+frame(0,0,w,h,False)
    x=28 if mobile else 34
    body+=text(x,39,'PSTAR80 / PRODUCT SHOWCASE',11,CYAN,650,extra='letter-spacing="1.9"')
    size=44 if mobile else 54
    body+=f'<text x="{x}" y="{94 if mobile else 105}" font-size="{size}" font-weight="700" fill="{WHITE}" opacity=".98">Sky<tspan fill="{CYAN}">Command</tspan></text>'
    body+=text(x,129 if mobile else 147,'Workflow Automation Platform',20 if mobile else 24,WHITE,600,extra='opacity=".97"')
    body+=text(x,158 if mobile else 178,'Deterministic Workflows · AI Agents',18 if mobile else 21,MUTED,400,extra='opacity=".96"')
    labels=['REUSABLE TOOLS','DURABLE WORKFLOWS','AI AGENTS','OBSERVABLE EXECUTION']
    for i,label in enumerate(labels):
        if mobile: xx=28+(i%2)*218; yy=302+(i//2)*44; bw=206; bh=32
        else: xx=34+i*226; yy=266; bw=214; bh=30
        body+=rect(xx,yy,bw,bh,'#041522','#26718A','fill-opacity=".78"')
        body+=text(xx+bw/2,yy+bh/2+4.5,label,12.8,CYAN,600,'middle')
    return doc(w,h,'SkyCommand — Workflow Automation Platform','Reusable Tools, Durable Workflows, AI Agents and Observable Execution. Full-width animated concept artwork, not an application screenshot or live telemetry.',body)

FEATURES=[
 ('Reusable Tools','Compose registered operations','with explicit inputs and results.','tools'),
 ('Published Workflows','Temporal-backed execution with','retries, scheduling and recovery.','flow'),
 ('AI Agents','Run embedded agents with','configured project capabilities.','agent'),
 ('External MCP Access','Coding assistants invoke operations','and inspect results through MCP.','mcp'),
 ('Structured Results','Inspect workflow and node outcomes','through structured outputs.','results'),
 ('Operational Visibility','Follow run history and diagnostics','from a shared operator interface.','visibility')]
ICONS={
 'tools':'<path d="M7 4L1 12l6 8M17 4l6 8-6 8M14 2l-4 20"/>',
 'flow':'<rect x="1" y="2" width="8" height="7"/><rect x="15" y="15" width="8" height="7"/><path d="M5 9v9h10"/>',
 'agent':'<rect x="3" y="6" width="18" height="15"/><path d="M12 6V2M8 11v4m8-4v4M8 18h8M0 11h3m18 0h3"/>',
 'mcp':'<path d="M8 3L1 12l7 9M16 3l7 9-7 9M8 12h8"/>',
 'results':'<rect x="4" y="1" width="16" height="22"/><path d="M8 7h8M8 12h8M8 17h5"/>',
 'visibility':'<path d="M1 12h5l3-9 5 18 3-9h6"/>'}
def features(mobile=False):
    w=480 if mobile else 960; cw=480 if mobile else 472
    h=6*140+5*16 if mobile else 3*154+2*16
    body=''
    for i,(title,line1,line2,ico) in enumerate(FEATURES):
        x=0 if mobile else (i%2)*488; y=i*156 if mobile else (i//2)*170
        ch=140 if mobile else 154
        body+=f'<g id="feature-{ico}">'+frame(x,y,cw,ch)
        body+=f'<g transform="translate({x+24} {y+23})" fill="none" stroke="{CYAN}" stroke-width="1.6" stroke-linejoin="round">{ICONS[ico]}</g>'
        body+=text(x+62,y+43,title,25,WHITE,650)
        body+=f'<path d="M{x+24} {y+62}H{x+cw-24}" stroke="#22485C"/>'
        body+=text(x+26,y+94,line1,20,MUTED)+text(x+26,y+122,line2,20,MUTED)
        body+='</g>'
    return doc(w,h,'SkyCommand — Key Capabilities','Reusable Tools, Published Workflows, AI Agents, External MCP Access, Structured Results and Operational Visibility.',body)

def node(id,x,y,w,h,labels,size=23):
    labels=[labels] if isinstance(labels,str) else labels
    out=f'<g id="{id}">'+rect(x,y,w,h,extra='stroke-width="1.5"')
    first=y+h/2-(len(labels)-1)*12+size*.35
    for i,label in enumerate(labels):out+=text(x+w/2,first+i*24,label,size,WHITE,600,'middle')
    return out+'</g>'
def edge(d):
    return f'<path d="{d}" fill="none" stroke="#25B8D6" stroke-width="2" marker-end="url(#arrow)"/><path d="{d}" fill="none" stroke="#D8FAFF" stroke-width="2" opacity=".65" pathLength="100" stroke-dasharray="7 93" class="stream"/>'
def architecture(mobile=False):
    w,h=(480,650) if mobile else (960,530)
    b=frame(0,0,w,h)+text(26,43,'Platform Architecture',25,WHITE,650)+f'<path d="M25 62H{w-25}" stroke="#22485C"/>'
    if mobile:
        b+=edge('M122 144V166H154V190')+edge('M358 144V166H326V190')
        b+=edge('M240 250V294')+edge('M240 418V464')
        b+=node('operator',24,88,196,56,'Operator',22)+node('coding-agents',260,88,196,56,'Coding Agents',22)
        b+=node('shared-access',42,190,396,60,'React UI / Node.js Core API',22)
        cy,ey=294,464;gx,gw=16,448
        b+=rect(gx,cy,gw,124,'#061521','#39788E')+text(32,cy+27,'Execution Capabilities',16,MUTED,500)
        for i,(id,lbl) in enumerate([('tools',['Registered','Tools']),('agents',['AI','Agents']),('workflows',['Published','Workflows'])]):b+=node(id,28+i*144,cy+46,136,60,lbl,19)
        b+=rect(gx,ey,gw,164,'#061521','#39788E')+text(32,ey+27,'Automation Endpoints',16,MUTED,500)
        for id,x,y,lbl in [('files',28,ey+42,'File System'),('database',28,ey+104,'Database'),('git',246,ey+42,'Git Repositories'),('web',246,ey+104,'Web APIs')]:b+=node(id,x,y,206,44,lbl,20)
    else:
        b+=edge('M247 140V159H365V180')+edge('M713 140V159H595V180')
        b+=edge('M480 238V280')+edge('M480 392V434')
        b+=node('operator',88,88,318,52,'Operator',24)+node('coding-agents',554,88,318,52,'External Coding Agents',24)
        b+=node('shared-access',200,180,560,58,'React UI / Node.js Core API',25)
        b+=rect(26,280,908,112,'#061521','#39788E')+text(42,307,'Execution Capabilities',16,MUTED,500)
        for i,(id,lbl) in enumerate([('tools','Registered Tools'),('agents','AI Agents'),('workflows','Published Workflows')]):b+=node(id,42+i*300,322,276,50,lbl,23)
        b+=rect(26,434,908,76,'#061521','#39788E')+text(42,457,'Automation Endpoints',16,MUTED,500)
        for i,(id,lbl) in enumerate([('files','File System'),('database','Database'),('git','Git Repositories'),('web','Web APIs')]):b+=node(id,42+i*223,468,207,28,lbl,21)
    return doc(w,h,'SkyCommand — Platform Architecture','Operators and configured coding agents use shared UI/API services, including MCP access for coding agents. Registered Tools, AI Agents and Published Workflows form the execution layer. Automation can operate on File System, Database, Git Repositories and Web APIs within configured permissions. Conceptual diagram, not a deployment specification or live status.',b)

def freeze(s):
    root=ET.fromstring(s)
    for parent in list(root.iter()):
        for child in list(parent):
            if child.tag.rsplit('}',1)[-1] in ('style','animate','animateTransform','animateMotion','set'):parent.remove(child)
        parent.attrib.pop('style',None)
        c=parent.get('class','').split()
        if 'halo' in c:parent.set('opacity','.16')
        if 'sweep' in c:parent.set('opacity','.45')
        if 'spark' in c:parent.set('opacity','.6')
    root.set('data-motion','static')
    d=root.find(f'{{{SVG}}}desc');d.text=(d.text or '')+' Static reduced-motion version.'
    return ET.tostring(root,encoding='unicode')+'\n'

def build(root:Path):
    src=root/'assets/brand/hero.svg'
    raw=src.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if blob!='fde1dd1a9c018d12678c46efddec1b72143db038':raise ValueError('Hero changed since review; refusing to overwrite')
    old=ET.fromstring(raw)
    art=old.find(f'.//{{{SVG}}}image').get('href')
    if not art or not art.startswith('data:image/png;base64,'):raise ValueError('Expected approved embedded PNG artwork')
    outputs={}
    for name,fn in [('hero',lambda m:hero(art,m)),('capabilities',features),('architecture',architecture)]:
        for mobile in [False,True]:
            stem=name+('-mobile' if mobile else '')
            animated=fn(mobile);ET.fromstring(animated)
            outputs[f'assets/brand/{stem}.svg']=animated
            outputs[f'assets/brand/{stem}-static.svg']=freeze(animated)
    for path,s in outputs.items():
        if 'Optional' in s:raise ValueError('Unexpected agent label')
        p=root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
    print(json.dumps({p:hashlib.sha256(s.encode()).hexdigest() for p,s in outputs.items()},indent=2))

if __name__=='__main__':build(Path('.'))
