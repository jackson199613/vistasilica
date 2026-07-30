# -*- coding: utf-8 -*-
import re, os
from tds_data import GRADES, PROPS, PAGE_GRADES, DISCLAIMER

SRC = "/home/claude/vistachem/resources/selector.html"
OUT = "/home/claude/vistachem/resources/specifications.html"
html = open(SRC).read()

# 提取 header（<body> 到 </header>）和 footer（<footer 到 </html>）
header = html[html.index("<body>"): html.index("</header>")+len("</header>")]
footer = html[html.index("<footer"):]

# GA 代码（从 selector 的 head 里提取）
ga = ""
m = re.search(r'<!-- Google Analytics.*?</script>\s*<script>.*?</script>', html, re.DOTALL)
if m: ga = m.group(0)

# 全牌号顺序（7个）
order = ["VS-C200","VS-F120","VS-A070","VS-T400","VS-WG180","VS-OE550","VS-P200"]

# 物性对比表
ths = "".join(f'<th>{GRADES[k]["name"]}</th>' for k in order)
rows = []
for i,(pname,unit,method) in enumerate(PROPS):
    vals = "".join(f"<td>{GRADES[k]['values'][i]}</td>" for k in order)
    rows.append(f"<tr><td>{pname}</td><td>{unit}</td>{vals}<td>{method}</td></tr>")
proptable = f'''<div class="tablewrap"><table class="data">
<thead><tr><th>Property</th><th>Unit</th>{ths}<th>Test method</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div>'''

# 应用映射表
approws = "".join(
    f'<tr><td><strong>{GRADES[k]["name"]}</strong></td><td>{GRADES[k]["track"]}</td><td>{GRADES[k]["use"]}</td><td>{GRADES[k]["focus"]}</td></tr>'
    for k in order)
apptable = f'''<div class="tablewrap"><table class="data">
<thead><tr><th>Grade</th><th>Application track</th><th>Typical use</th><th>Key performance focus</th></tr></thead>
<tbody>{approws}</tbody></table></div>'''

# 合规信息
compliance = '''<ul class="check-list">
<li><strong>REACH:</strong> Registered under EINECS 231-545-4 (silicic acid)</li>
<li><strong>Food additive (EU):</strong> E 551 — Reg. (EU) No 231/2012 (food-grade grades only)</li>
<li><strong>Food additive (US):</strong> 21 CFR § 172.480 (food-grade grades only)</li>
<li><strong>Feed material:</strong> Listed in EU Register of Feed Materials (silicic acid, precipitated)</li>
<li><strong>Cosmetics (EU):</strong> INCI: Hydrated Silica — Reg. (EC) No 1223/2009</li>
<li><strong>Nano status:</strong> Not a nanomaterial as defined by EU 2015/2283</li>
<li><strong>Hazard classification:</strong> Not classified as hazardous per CLP Reg. (EC) 1272/2008</li>
<li><strong>Kosher / Halal:</strong> Available upon request (food-grade grades)</li>
</ul>'''

# 重金属表
hm = '''<div class="tablewrap"><table class="data">
<thead><tr><th>Parameter</th><th>Unit</th><th>Typical max</th><th>Reference limit</th></tr></thead>
<tbody>
<tr><td>Lead (Pb)</td><td>mg/kg</td><td>≤ 5</td><td>FCC / EU 231/2012: ≤ 5 ppm</td></tr>
<tr><td>Arsenic (As)</td><td>mg/kg</td><td>≤ 3</td><td>FCC / EU 231/2012: ≤ 3 ppm</td></tr>
<tr><td>Cadmium (Cd)</td><td>mg/kg</td><td>≤ 1</td><td>Industry standard: ≤ 1 ppm</td></tr>
<tr><td>Mercury (Hg)</td><td>mg/kg</td><td>≤ 1</td><td>FCC / EU 231/2012: ≤ 1 ppm</td></tr>
<tr><td>Heavy metals (as Pb, total)</td><td>mg/kg</td><td>≤ 10</td><td>FCC: ≤ 10 ppm</td></tr>
</tbody></table></div>'''

# 包装
packaging = '''<ul class="check-list">
<li><strong>20 kg paper bag</strong> — 3-ply kraft with inner PE liner, standard export packaging</li>
<li><strong>25 kg paper bag</strong> — 3-ply kraft with inner PE liner, palletized and stretch-wrapped</li>
<li><strong>500 kg big bag (FIBC)</strong> — Type C or D with PE inner liner, bulk industrial shipments</li>
<li><strong>1,000 kg big bag (FIBC)</strong> — Type C or D with PE inner liner, bulk industrial shipments</li>
</ul>'''

# 页面主体
main = f'''
<main>
  <section class="page-hero page-hero--dark">
    <div class="wrap">
      <span class="eyebrow">Technical data</span>
      <h1>Precipitated silica — grade specifications</h1>
      <p class="lead">Vistasilica precipitated silica is a synthetic amorphous silica (SiO₂·nH₂O, CAS 112945-52-5) produced by controlled precipitation. The grade family below spans feed additives, food powders, oral care, agrochemical, edible oil refining and personal care — each differentiated by surface area, particle size and absorption to match the target application.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="notice" style="background:var(--sand-2,#f5ecd8);border-left:3px solid var(--sand,#c8a86a);padding:1rem 1.25rem;border-radius:8px;margin-bottom:2rem;font-size:.9rem">
        <strong>Preliminary data.</strong> {DISCLAIMER}
      </div>

      <h2>Typical physical properties — grade family comparison</h2>
      {proptable}

      <h2 style="margin-top:3rem">Grade application map</h2>
      {apptable}

      <h2 style="margin-top:3rem">Regulatory &amp; compliance</h2>
      {compliance}

      <h2 style="margin-top:2.5rem">Typical heavy-metal content (food / feed grade)</h2>
      {hm}

      <h2 style="margin-top:3rem">Packaging</h2>
      {packaging}

      <div class="cta-band" style="margin-top:3rem;padding:2rem;background:var(--ink);border-radius:14px;text-align:center">
        <h3 style="color:#fff;margin-bottom:.75rem">Need a grade-specific TDS or a sample?</h3>
        <p style="color:rgba(255,255,255,.7);margin-bottom:1.5rem">Tell us your application track, process system and target metrics — we'll confirm the right grade direction and provide samples with documentation.</p>
        <a class="btn btn--primary" href="sample.html">Request a sample</a>
        <a class="btn btn--ghost-light" href="../contact.html" style="margin-left:.75rem">Talk to an expert</a>
      </div>
    </div>
  </section>
</main>
'''

# Product schema for all grades (ItemList)
import json
items = []
for idx,k in enumerate(order,1):
    g = GRADES[k]
    add = [{"@type":"PropertyValue","name":p[0],"value":g['values'][i],"unitText":p[1],"measurementTechnique":p[2]} for i,p in enumerate(PROPS)]
    items.append({"@type":"ListItem","position":idx,"item":{
        "@type":"Product","name":f"Vistasilica {g['name']}","category":"Precipitated silica",
        "brand":{"@type":"Brand","name":"Vistasilica"},"additionalProperty":add,
        "material":"Synthetic amorphous precipitated silica (CAS 112945-52-5)"}})
schema = {"@context":"https://schema.org","@type":"ItemList","name":"Vistasilica precipitated silica grades","itemListElement":items}
schema_block = '<script type="application/ld+json">\n'+json.dumps(schema,ensure_ascii=False,indent=2)+'\n</script>'

# head
head = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Silica Grade Specifications &amp; TDS | Vistasilica</title>
<meta name="description" content="Vistasilica precipitated silica grade specifications: BET surface area, oil absorption, particle size, density and purity across seven grades for feed, food, oral care, agrochemical, oil refining and personal care. Typical values with ISO test methods.">
<meta property="og:title" content="Silica Grade Specifications & TDS | Vistasilica">
<meta property="og:description" content="Precipitated silica grade family — typical physical properties, application map, compliance and packaging.">
<meta property="og:type" content="website">
<link rel="icon" href="../assets/img/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/apple-refine.css">
{schema_block}
{ga}
</head>
'''

page = head + header + main + footer
open(OUT,'w').write(page)
print(f"✓ 生成 {OUT}")
print(f"  字节数: {len(page)}")
