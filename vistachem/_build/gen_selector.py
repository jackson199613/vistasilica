# -*- coding: utf-8 -*-
# 把真实牌号+关键参数接进选型器
import re

SEL = "/home/claude/vistachem/resources/selector.html"
html = open(SEL).read()

# 每行映射：(现有的 grade-tag 文本) -> (真实牌号, 关键参数简述)
# 按表格顺序对应
ROW_MAP = [
    # Feed additives
    ("Carrier · high absorption", "VS-C200", "Oil abs. 240–290 g/100g · BET 170–230 m²/g"),
    ("Flow aid · fine", "VS-F120", "BET 100–150 m²/g · D50 5–12 µm"),
    # Food powders
    ("Food grade · anti-caking", "VS-F120", "D50 5–12 µm · 45µm residue ≤0.05%"),
    ("High surface · carrier", "VS-C200", "Oil abs. 240–290 g/100g · BET 170–230 m²/g"),
    # Oral care
    ("Abrasive", "VS-A070", "BET 45–90 m²/g · D50 6–12 µm (controlled RDA)"),
    ("Thickener", "VS-T400", "BET 350–450 m²/g · oil abs. 260–310 g/100g"),
    # Agrochemical
    ("WP inert carrier", "VS-WG180", "Oil abs. 200–250 g/100g · bulk 100–160 g/L"),
    ("WG disintegrating", "VS-WG180", "D50 12–22 µm · BET 160–210 m²/g"),
    ("SC rheology / anti-caking", "VS-WG180", "BET 160–210 m²/g · anti-caking / rheology"),
    # Oil refining
    ("Silica gel · dephosphorization", "VS-OE550", "BET 400–600 m²/g · oil abs. 180–260 g/100g"),
    ("Filtration enhancing", "VS-OE550", "BET 400–600 m²/g · bulk 350–500 g/L"),
    # Personal care
    ("High oil absorption", "VS-P200", "Oil abs. 220–270 g/100g · D50 3–8 µm"),
    ("Spherical · soft focus", "VS-P200", "D50 3–8 µm · BET 180–240 m²/g"),
]

# 1. 改表头：Recommended grade -> Grade + Key spec
html = html.replace(
    "<thead><tr><th>Track</th><th>Application system</th><th>Key metrics</th><th>Recommended grade</th><th>Solution</th></tr></thead>",
    "<thead><tr><th>Track</th><th>Application system</th><th>Key metrics</th><th>Grade</th><th>Typical key spec</th><th>Solution</th></tr></thead>"
)

# 2. 逐行替换 grade-tag → 牌号 + 新增参数列
for tag_text, grade, spec in ROW_MAP:
    old = f'<td><span class="grade-tag">{tag_text}</span></td>'
    new = f'<td><span class="grade-tag">{grade}</span></td><td style="font-size:.82rem">{spec}</td>'
    # 只替换第一次出现（按顺序）
    idx = html.find(old)
    if idx >= 0:
        html = html[:idx] + new + html[idx+len(old):]
    else:
        print(f"  未找到: {tag_text}")

# 3. 更新说明文字，提到具体牌号
html = html.replace(
    "Lock the application by track, then read the key metrics and recommended grade direction. This is directional selection — final grades depend on your actual process conditions and test feedback.",
    "Lock the application by track, then read the key metrics, matching grade and typical key specification. This is directional selection — final grades depend on your actual process conditions and test feedback. See the full <a href=\"specifications.html\" style=\"color:var(--teal)\">grade specifications</a> for complete data."
)

open(SEL, 'w').write(html)
print("选型器已接入真实牌号 + 参数")
# 验证
print("VS- 牌号出现次数:", html.count('grade-tag">VS-'))
