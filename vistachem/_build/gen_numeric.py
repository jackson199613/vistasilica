# -*- coding: utf-8 -*-
# 给方案页核心价值段增补一条"数值化"支撑句（GEO：数值可被 AI 引用）
import os

BASE = "/home/claude/vistachem/solutions"

# page -> 数值化支撑句（基于真实 TDS，每段自洽、带具体数值和牌号）
NUMERIC = {
    "feed-additives": 'On <strong>VS-C200</strong>, an oil absorption of <strong>240–290 g/100g</strong> (ISO 4652) and BET surface area of <strong>170–230 m²/g</strong> (ISO 9277) support high liquid loading and carrier capacity for premix and liquid-additive powdering.',
    "food-powder": 'On <strong>VS-F120</strong>, a fine particle size (D50 <strong>5–12 µm</strong>, ISO 13320) with 45 µm sieve residue <strong>≤ 0.05%</strong> (ISO 2591-1) supports free flow and anti-caking in seasoning powders and dry blends.',
    "oral-care": 'Two grades cover the two lines: <strong>VS-A070</strong> (BET <strong>45–90 m²/g</strong>) for controlled-RDA cleaning abrasion, and <strong>VS-T400</strong> (BET <strong>350–450 m²/g</strong>, oil absorption <strong>260–310 g/100g</strong>) for thickening and paste structure.',
    "agro": 'On <strong>VS-WG180</strong>, an oil absorption of <strong>200–250 g/100g</strong> with poured bulk density <strong>100–160 g/L</strong> (ISO 60) supports active loading and disintegration in WP/WG carriers and SC anti-caking / rheology control.',
    "oil-refining": 'On <strong>VS-OE550</strong>, a high BET surface area of <strong>400–600 m²/g</strong> (ISO 9277) with oil absorption <strong>180–260 g/100g</strong> supports phospholipid and soap adsorption in degumming and filtration.',
    "personal-care": 'On <strong>VS-P200</strong>, an oil absorption of <strong>220–270 g/100g</strong> with fine particle size (D50 <strong>3–8 µm</strong>, ISO 13320) supports oil control, matte finish and a soft-focus skin feel in color cosmetics.',
}

count = 0
for page, sentence in NUMERIC.items():
    path = os.path.join(BASE, f"{page}.html")
    html = open(path).read()
    if 'data-numeric-support' in html:
        continue  # 已加
    # 在 Core value 的 </ul> 后加一个数值化补充段
    marker = '<h2>Core value</h2>'
    idx = html.find(marker)
    if idx < 0:
        print(f"  {page}: 未找到 Core value"); continue
    ul_end = html.find('</ul>', idx) + len('</ul>')
    support = f'\n        <p data-numeric-support style="margin-top:.9rem;padding:.9rem 1.1rem;background:var(--wash,#f4f7f6);border-left:3px solid var(--teal);border-radius:8px;font-size:.9rem">{sentence}</p>'
    html = html[:ul_end] + support + html[ul_end:]
    open(path, 'w').write(html)
    count += 1
    print(f"✓ {page}")

print(f"\n完成 {count} 个方案页文案数值化")
