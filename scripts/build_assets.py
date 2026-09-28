"""Build self-contained SVG profile artwork and a local layout preview."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)

header = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="440" viewBox="0 0 1200 440" role="img" aria-labelledby="title desc">
<title id="title">Deshan Dinidu</title><desc id="desc">Building ideas into working software. TypeScript, JavaScript, Node.js and .NET.</desc>
<defs>
 <linearGradient id="bg" x2="1" y2="1"><stop stop-color="#101f35"/><stop offset="1" stop-color="#080e1b"/></linearGradient>
 <linearGradient id="accent"><stop stop-color="#67e8f9"/><stop offset="1" stop-color="#818cf8"/></linearGradient>
 <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#a5c9ee" stroke-opacity=".045"/></pattern>
</defs>
<style>
 .orbit{transform-origin:974px 211px;animation:turn 28s linear infinite}.pulse{animation:pulse 3s ease-in-out infinite}
 @keyframes turn{to{transform:rotate(360deg)}}@keyframes pulse{50%{opacity:.3}}
 @media(prefers-reduced-motion:reduce){.orbit,.pulse{animation:none}}
 text{font-family:Arial,Helvetica,sans-serif}
</style>
<rect width="1200" height="440" rx="24" fill="url(#bg)"/>
<rect width="1200" height="440" rx="24" fill="url(#grid)"/>
<path d="M48 0H1152" stroke="url(#accent)" stroke-width="3"/>
<circle cx="61" cy="61" r="5" fill="#67e8f9" class="pulse"/>
<text x="78" y="66" font-size="13" letter-spacing="3" fill="#94a9c4">DESHAN / DEVELOPER</text>
<text x="54" y="162" font-size="74" font-weight="700" letter-spacing="-3" fill="#f1f5f9">Deshan Dinidu<tspan fill="#67e8f9">.</tspan></text>
<text x="58" y="215" font-size="27" fill="#cbd5e1">Building ideas into</text>
<text x="58" y="253" font-size="27" fill="#67e8f9">working software.</text>
<path d="M58 294H704" stroke="#24364d"/>
<text x="58" y="332" font-size="15" fill="#94a9c4" letter-spacing="1">REACT   /   NEXT.JS   /   NODE.JS   /   REACT NATIVE   /   AWS</text>
<text x="58" y="391" font-size="12" fill="#647a99" letter-spacing="2">EXPLORE THE WORK BELOW ↓</text>
<circle cx="974" cy="211" r="151" fill="none" stroke="#1d3049"/>
<circle cx="974" cy="211" r="114" fill="none" stroke="#243e58" stroke-dasharray="4 10"/>
<g class="orbit"><ellipse cx="974" cy="211" rx="150" ry="64" transform="rotate(-35 974 211)" fill="none" stroke="#67e8f9" stroke-opacity=".45"/><circle cx="851" cy="297" r="6" fill="#67e8f9"/></g>
<rect x="903" y="140" width="142" height="142" rx="32" fill="#101e32" stroke="#3c5877" transform="rotate(-8 974 211)"/>
<text x="974" y="232" text-anchor="middle" font-size="58" font-weight="700" fill="url(#accent)">&lt;/&gt;</text>
<text x="974" y="401" text-anchor="middle" font-size="11" letter-spacing="2" fill="#647a99">DESHANDINIDU2001</text>
</svg>'''
(ASSETS / 'header.svg').write_text(header, encoding='utf-8')

projects = [
 ('spectraleaf', '01', 'SpectraLeaf', 'Tea fermentation monitoring. Web, mobile and cloud.', 'NEXT.JS  /  REACT NATIVE  /  EXPRESS  /  DYNAMODB', 'https://github.com/cepdnaclk/e21-3yp-SPECTRA-LEAF', '#67e8f9'),
 ('ran-technology', '02', 'RAN Technology', 'Explore the project and source code.', 'TYPESCRIPT', 'RAN-Technology-', '#a5b4fc'),
 ('smartloan', '03', 'Smartloan BLMS', 'Explore the project and source code.', 'JAVASCRIPT', 'Smartloan_BLMS', '#86efac'),
 ('game-cafe', '04', 'Gaming Café', 'Session management. Connected Windows clients.', 'TYPESCRIPT  /  NODE.JS  /  .NET', 'game-cafe-new', '#fcd34d'),
]
for slug, number, title, subtitle, stack, repo, accent in projects:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="190" viewBox="0 0 1200 190" role="img" aria-label="{escape(title)}">
    <rect x="1" y="1" width="1198" height="188" rx="18" fill="#0d1728" stroke="#26374d"/>
    <rect x="1" y="35" width="3" height="120" rx="1" fill="{accent}"/>
    <g font-family="Arial,Helvetica,sans-serif">
    <text x="36" y="57" font-size="16" fill="{accent}">{number}</text>
    <text x="92" y="62" font-size="29" font-weight="700" fill="#f1f5f9">{escape(title)}</text>
    <text x="92" y="101" font-size="19" fill="#a4b5cb">{escape(subtitle)}</text>
    <text x="92" y="151" font-size="12" letter-spacing="2" fill="{accent}">{stack}</text>
    <text x="1139" y="65" font-size="30" text-anchor="end" fill="{accent}">↗</text>
    <text x="1139" y="152" font-size="12" letter-spacing="2" text-anchor="end" fill="#859ab5">VIEW SOURCE</text>
    </g></svg>'''
    (ASSETS / f'{slug}.svg').write_text(svg, encoding='utf-8')

cards = ''.join(f'<a href="{p[5] if p[5].startswith("https://") else "https://github.com/deshandinidu2001/" + p[5]}"><img src="assets/{p[0]}.svg" alt="{escape(p[2])}"></a>' for p in projects)
preview = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Deshan Dinidu · Profile preview</title>
<style>*{box-sizing:border-box}body{margin:0;background:#070d17;color:#cad5e4;font:16px/1.7 system-ui,sans-serif}main{max-width:1000px;margin:40px auto;padding:32px;border:1px solid #26374d;border-radius:16px;background:#0b1220}img{display:block;width:100%;height:auto}a{color:#67e8f9;text-decoration:none}a:hover{color:#b4f4ff}nav{text-align:center;padding:22px}h2{font-size:23px;color:#f1f5f9;margin-top:35px;border-bottom:1px solid #26374d;padding-bottom:10px}.cards{display:grid;gap:18px}details{border:1px solid #26374d;border-radius:10px;padding:16px;margin:20px 0}summary{cursor:pointer}.tags{display:flex;gap:10px;flex-wrap:wrap}.tags span{padding:5px 15px;border:1px solid #31445e;border-radius:6px;color:#b7eaf6}footer{text-align:center;margin-top:45px;color:#859ab5;font-size:13px}.note{font-size:12px;color:#859ab5;text-align:center}@media(max-width:600px){main{margin:0;padding:18px;border:0;border-radius:0}nav{font-size:13px}}</style>
<main><p class="note">Local design preview · GitHub controls the final page typography and layout.</p><img src="assets/header.svg" alt="Deshan Dinidu — building ideas into working software"><nav><a href="#work">Selected work</a> &nbsp; / &nbsp; <a href="#toolkit">Toolkit</a> &nbsp; / &nbsp; <a href="https://github.com/deshandinidu2001?tab=repositories">All repositories ↗</a></nav><h2>A little about me</h2><p>Hi, I'm <strong>Deshan</strong>. I build across web, mobile, and backend systems with TypeScript and JavaScript. I'm part of the <strong>SpectraLeaf</strong> team, developing an IoT-based tea fermentation monitoring project with web and mobile applications.</p><p>I enjoy turning ideas into practical software, connecting interfaces to the systems behind them, and learning through building.</p><h2>Education</h2><p><strong>University of Peradeniya, Sri Lanka</strong><br>Faculty of Engineering · Department of Computer Engineering</p><p><strong>Degree programme:</strong> Bachelor of the Science of Engineering Honours (BScEngHons) — Computer Engineering<br><strong>Batch:</strong> E21</p><p><a href="https://people.ce.pdn.ac.lk/students/e21/054/">View my university profile ↗</a></p><h2 id="work">Selected work</h2><div class="cards">''' + cards + '''</div><details><summary>Explore the gaming café system</summary><p>A Node.js server manages session timers and sends lock/unlock commands to .NET 8 Windows clients over TCP using JSON messages.</p><a href="https://github.com/deshandinidu2001/game-cafe-new">Explore the code →</a></details><h2 id="toolkit">Toolkit</h2><p>Technologies used across my featured public projects:</p><div class="tags"><span>TypeScript</span><span>JavaScript</span><span>React</span><span>Next.js</span><span>GSAP</span><span>Zustand</span><span>React Native</span><span>Expo</span><span>Node.js</span><span>Express</span><span>.NET</span><span>AWS SDK</span><span>DynamoDB</span><span>AWS Amplify</span></div><details><summary>More from my workbench</summary><a href="https://github.com/deshandinidu2001/Peraverse_Kiosk-main">Peraverse Kiosk →</a></details><footer>IDEAS → CODE → SOMETHING USEFUL<br><a href="https://github.com/deshandinidu2001">Find me on GitHub ↗</a></footer></main></html>'''
(ROOT / 'preview.html').write_text(preview, encoding='utf-8')
print('Built five SVG assets and preview.html')
