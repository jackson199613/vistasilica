# -*- coding: utf-8 -*-
import json, re, os
from tds_data import GRADES, PROPS, PAGE_GRADES, DISCLAIMER

SITE = "https://vistasilica.com"
BASE = "/home/claude/vistachem/solutions"

def props_table_html(grade_keys):
    """正文可见的典型物性表（AI 按段可读，数值写进 HTML 正文）"""
    grades = [GRADES[k] for k in grade_keys]
    # 表头
    ths = "".join(f"<th>{g['name']}</th>" for g in grades)
    header = f"<thead><tr><th>Property</th><th>Unit</th>{ths}<th>Test method</th></tr></thead>"
    rows = []
    for i, (pname, unit, method) in enumerate(PROPS):
        vals = "".join(f"<td>{g['values'][i]}</td>" for g in grades)
        rows.append(f"<tr><td>{pname}</td><td>{unit}</td>{vals}<td>{method}</td></tr>")
    body = "<tbody>" + "".join(rows) + "</tbody>"
    intro_grades = ", ".join(g['name'] for g in grades)
    # 每段自洽：首句带完整主语（GEO 要求）
    lead = (f"Vistasilica {grade_keys[0].split('-')[0]}-series precipitated silica for this track "
            f"is offered as {intro_grades}. Typical physical properties are shown below with the "
            f"applicable test method for each parameter.")
    return f'''
        <h2>Typical properties</h2>
        <p style="margin-bottom:1rem">{lead}</p>
        <div class="tablewrap">
          <table class="data">
            {header}
            {body}
          </table>
        </div>
        <p style="font-size:.82rem;color:var(--ink-3);margin-top:.75rem"><strong>Preliminary — not specifications.</strong> {DISCLAIMER}</p>
'''

def product_schema(grade_keys, page):
    """Product schema，additionalProperty 承载物性；如实标注 typical/preliminary"""
    schemas = []
    for k in grade_keys:
        g = GRADES[k]
        add_props = []
        for i, (pname, unit, method) in enumerate(PROPS):
            add_props.append({
                "@type": "PropertyValue",
                "name": pname,
                "value": g['values'][i],
                "unitText": unit,
                "measurementTechnique": method
            })
        schema = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": f"Vistasilica {g['name']} — Precipitated Silica",
            "category": "Precipitated silica / Synthetic amorphous silica",
            "description": f"{g['use']}. Key performance focus: {g['focus']}. Typical/preliminary values based on industry reference data pending laboratory validation.",
            "brand": {"@type": "Brand", "name": "Vistasilica"},
            "manufacturer": {"@type": "Organization", "name": "Vistasilica", "description": "A Vista brand"},
            "material": "Synthetic amorphous precipitated silica (SiO₂·nH₂O, CAS 112945-52-5)",
            "additionalProperty": add_props,
            "url": f"{SITE}/solutions/{page}.html"
        }
        schemas.append(schema)
    return schemas

count = 0
for page, keys in PAGE_GRADES.items():
    path = os.path.join(BASE, f"{page}.html")
    if not os.path.exists(path):
        print(f"跳过(不存在): {page}"); continue
    html = open(path).read()

    # 1. 插入正文参数表（在 "Validation guide" 前）
    if "Typical properties" not in html:
        table = props_table_html(keys)
        html = html.replace('        <h2>Validation guide</h2>', table + '\n        <h2>Validation guide</h2>', 1)

    # 2. 插入 Product schema（在 </head> 前）
    if '"@type": "Product"' not in html and '"@type":"Product"' not in html:
        schemas = product_schema(keys, page)
        blocks = "\n".join(
            '<script type="application/ld+json">\n' + json.dumps(s, ensure_ascii=False, indent=2) + '\n</script>'
            for s in schemas
        )
        html = html.replace('</head>', blocks + '\n</head>', 1)

    open(path, 'w').write(html)
    count += 1
    print(f"✓ {page}.html — 参数表 + {len(keys)} 个 Product schema")

print(f"\n完成 {count} 个方案页")
