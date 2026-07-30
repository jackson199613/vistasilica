# -*- coding: utf-8 -*-
# 内链优化：方案页加"相关方案 + 规格/选型"链接区块
import os

BASE = "/home/claude/vistachem/solutions"

# 每个方案页的相关方案（基于应用逻辑相关性）
RELATED = {
    "feed-additives": [("food-powder", "Food Powder Flow", "similar flow & anti-caking principles"),
                       ("agro", "Agrochemical Carrier", "carrier & absorption logic")],
    "food-powder": [("feed-additives", "Feed Additive Flow & Carrier", "shared flow & carrier technology"),
                    ("personal-care", "Personal Care Mattifying", "fine-particle powder handling")],
    "oral-care": [("personal-care", "Personal Care Mattifying", "cosmetic-grade silica"),
                  ("food-powder", "Food Powder Flow", "food-contact grades")],
    "agro": [("feed-additives", "Feed Additive Flow & Carrier", "inert carrier & absorption"),
             ("oil-refining", "Edible Oil Refining", "adsorption & filtration")],
    "oil-refining": [("agro", "Agrochemical Carrier", "high-surface adsorption grades"),
                     ("personal-care", "Personal Care Mattifying", "oil-absorption grades")],
    "personal-care": [("oral-care", "Oral Care Silica", "cosmetic & oral-care grades"),
                      ("food-powder", "Food Powder Flow", "fine-particle handling")],
}

count = 0
for page, rels in RELATED.items():
    path = os.path.join(BASE, f"{page}.html")
    html = open(path).read()
    if 'data-related-links' in html:
        continue
    # 构建相关链接卡片
    rel_cards = "".join(
        f'<a href="{p}.html" class="related-card"><strong>{name}</strong><span>{why}</span></a>'
        for p, name, why in rels
    )
    block = f'''
        <div data-related-links style="margin-top:2.5rem">
          <h2>Related solutions &amp; data</h2>
          <div class="related-grid">
            {rel_cards}
            <a href="../resources/specifications.html" class="related-card related-card--accent"><strong>Grade specifications</strong><span>Full TDS: properties, compliance, packaging</span></a>
            <a href="../resources/selector.html" class="related-card related-card--accent"><strong>Product selector</strong><span>Match application → grade → key spec</span></a>
          </div>
        </div>'''
    # 插在 Technical service 段之前（如果有），否则在 </main> 前
    if '<h2>Technical service</h2>' in html:
        html = html.replace('<h2>Technical service</h2>', block + '\n\n        <h2>Technical service</h2>', 1)
    else:
        html = html.replace('</main>', block + '\n</main>', 1)
    open(path, 'w').write(html)
    count += 1
    print(f"✓ {page}: +{len(rels)} 相关方案 + 2 资源链接")

print(f"\n完成 {count} 个方案页内链")
