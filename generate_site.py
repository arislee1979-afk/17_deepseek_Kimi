#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeepSeek Research Portal HTML Generator
Converts all project markdown documents into a cohesive, modern glassmorphism Dark Tech Web App.
Uses zero external dependencies beyond standard python markdown library.
"""

import os
import re
import markdown

# Markdown is source of truth. Every entry must exist or build fails.
DOCS = [
    {
        "file": "01_speech.md",
        "html": "01_speech.html",
        "title": "01_speech · 梁文鋒四小時交流發言精校",
        "short_title": "01_ 發言精校原文",
        "tag": "LEAD / UNVERIFIED",
        "tag_class": "badge-analysis",
        "desc": "未驗證外傳轉寫（非官方）。開源、剋制、十個月回本（payback）、AGI 路線等主張的原始載體。"
    },
    {
        "file": "02_speech_deep_analysis.md",
        "html": "02_speech_deep_analysis.html",
        "title": "02_speech_deep_analysis · 梁文鋒講話心智模型拆解",
        "short_title": "02_ 講話心智模型拆解",
        "tag": "ANALYSIS",
        "tag_class": "badge-analysis",
        "desc": "將外傳發言提煉為戰略心智模型；payback≠淨利；TileLang 等為歸因主張。"
    },
    {
        "file": "03_StockWe_融資暫停串聯分析_核查.md",
        "html": "03_StockWe_融資暫停串聯分析_核查.html",
        "title": "03_StockWe_融資暫停串聯分析_核查 · 新聞事實邊界與產業評論評估",
        "short_title": "03_ 融資暫停事件核查",
        "tag": "EVIDENCE CHECK",
        "tag_class": "badge-live",
        "desc": "Bloomberg 單一匿名信源鏈；Reuters 轉載未獨立核實；StockWe 故事層分離。"
    },
    {
        "file": "04_viewpoint_克制對準與算力底褲.md",
        "html": "04_viewpoint_克制對準與算力底褲.html",
        "title": "04_viewpoint · 克制對準與算力底褲",
        "short_title": "04_ 觀點：克制對準與算力",
        "tag": "VIEWPOINT",
        "tag_class": "badge-analysis",
        "desc": "克制對準向量與算力硬約束；Eden「受限芯片」句已降為待查線索。"
    },
    {
        "file": "05_NVIDIA_SK_美國隊聯盟_分層相位與雙循環.md",
        "html": "05_NVIDIA_SK_美國隊聯盟_分層相位與雙循環.html",
        "title": "05_NVIDIA_SK · 美國隊聯盟與分層相位",
        "short_title": "05_ NVIDIA-SK 美國隊",
        "tag": "EVENT + FRAMEWORK",
        "tag_class": "badge-live",
        "desc": "以 NVIDIA 官方公告為 fact base 的 SK 合作詮釋；友岸 H 層綁定框架。"
    },
    {
        "file": "05_1_source_NVIDIA_SK_對話輿情轉寫.md",
        "html": "05_1_source_NVIDIA_SK_對話輿情轉寫.html",
        "title": "05_1_source · NVIDIA-SK 來源與有界輿情",
        "short_title": "05_1 來源與輿情",
        "tag": "SOURCE CAPTURE",
        "tag_class": "badge-live",
        "desc": "官方 URL、平行事件分列、單一 PTT 串樣本；Grok 對話不作為 fact source。"
    },
    {
        "file": "06_中美對立敘事_梁有意無意與兩隊結構.md",
        "html": "06_中美對立敘事_梁有意無意與兩隊結構.html",
        "title": "06 · 中美對立敘事與兩隊結構",
        "short_title": "06_ 兩隊觀點統合",
        "tag": "HYPOTHESIS（非 Synthesis）",
        "tag_class": "badge-analysis",
        "desc": "觀點統合：已知事實／歸因主張／工作假說三欄；非正式 Current Synthesis。"
    },
    {
        "file": "reviews/02_critic_review.md",
        "html": "02_critic_review.html",
        "title": "02_critic_review · Critic 批判與審查",
        "short_title": "02_ Critic 批判審查",
        "tag": "CRITIC（非必讀）",
        "tag_class": "badge-live",
        "desc": "針對深度拆解的 Critic 審查；格式已暫停，非必讀。"
    },
    {
        "file": "00_inbox.md",
        "html": "00_inbox.html",
        "title": "00_inbox · 研究收件箱與碎片資料庫",
        "short_title": "00_inbox 未分類資料",
        "tag": "INBOX",
        "tag_class": "badge-live",
        "desc": "尚未升級編入主線的新聞線索、推文與臨時觀察。"
    },
    {
        "file": "README.md",
        "html": "README.html",
        "title": "README · 專案綱領與當前狀態",
        "short_title": "README 專案綱領",
        "tag": "KNOWLEDGE HUB",
        "tag_class": "badge-live",
        "desc": "專案身份、證據矩陣、Open Question 與 Next Action。"
    },
    {
        "file": "AGENTS.md",
        "html": "AGENTS.html",
        "title": "AGENTS · 作業規則與多模型角色分工",
        "short_title": "AGENTS 作業規則",
        "tag": "GOVERNANCE",
        "tag_class": "badge-analysis",
        "desc": "作業紀律、來源分級與強制鏈接輸出規範。"
    }
]

# HTML pages that may exist but must be removed if no longer generated
ORPHAN_HTML_CANDIDATES = [
    "05_NVIDIA_SK_5000億美元AI合作與市場情緒核查.html",
]

def render_navbar(active_html=""):
    links_html = ""
    for doc in DOCS:
        active = "active" if doc["html"] == active_html else ""
        links_html += f'<li><a href="{doc["html"]}" class="nav-link {active}">{doc["short_title"]}</a></li>\n'
    
    return f"""
    <nav class="navbar">
      <div class="nav-content">
        <a href="index.html" class="logo">
          <div class="logo-icon">🧠</div>
          <span>DeepSeek Research Portal</span>
        </a>
        <ul class="nav-links">
          <li><a href="index.html" class="nav-link {'active' if active_html=='index.html' else ''}">首頁導航</a></li>
          {links_html}
        </ul>
        <div>
          <span class="badge badge-analysis">Stage: ANALYSIS</span>
        </div>
      </div>
    </nav>
    """

def render_footer():
    return """
    <footer class="footer">
      <div class="footer-links">
        <a href="index.html" class="footer-link">首頁 Dashboard</a>
        <a href="README.html" class="footer-link">專案 README</a>
        <a href="AGENTS.html" class="footer-link">作業規則</a>
        <a href="https://github.com/arislee1979-afk/17_deepseek_Kimi" target="_blank" class="footer-link">GitHub Repository</a>
      </div>
      <p>💡 本專案為知識研究 Repo，與 Hub (30_investment_hub) 保持階段索引。不構成投資或交易建議。</p>
      <p style="margin-top:0.5rem;font-size:0.8rem;color:#475569;">Generated by Antigravity · Silicon Dark Cyber Theme</p>
    </footer>
    """

def build_index():
    navbar = render_navbar("index.html")
    footer = render_footer()
    
    cards_html = ""
    for doc in DOCS:
        cards_html += f"""
        <a href="{doc['html']}" class="doc-card">
          <div>
            <div class="doc-card-header">
              <span class="doc-tag">{doc['tag']}</span>
              <span style="font-size:1.1rem;">↗</span>
            </div>
            <h3 class="doc-title">{doc['title'].split(' · ')[1] if ' · ' in doc['title'] else doc['title']}</h3>
            <p class="doc-desc">{doc['desc']}</p>
          </div>
          <div class="doc-footer">
            <span>文件代號: <code>{doc['file']}</code></span>
            <span>點擊瀏覽 →</span>
          </div>
        </a>
        """

    index_content = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DeepSeek 戰略心智與公開敘事研究中心 · Research Portal</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="bg-orbs">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
  </div>
  
  <div class="app-container">
    {navbar}
    
    <main class="main-content">
      <!-- Hero Section -->
      <section class="hero-section">
        <h1 class="hero-title">DeepSeek 戰略心智與<span>公開敘事研究中心</span></h1>
        <p class="hero-subtitle">
          深度拆解梁文鋒四小時交流稿的戰略心智模型，釐清「剋制即戰略」與開源商業邏輯；
          獨立核查第二輪融資暫停新聞的事實邊界，分離產業二手評論的事實層與故事層。
        </p>
        <div class="hero-meta">
          <span class="badge badge-analysis">Knowledge Stage: ANALYSIS</span>
          <span class="badge badge-live">Live HTML Documentation</span>
          <span class="badge badge-analysis">Canonical: /home/arislee1979/0_project/17_deepseek_Kimi</span>
        </div>
      </section>
      
      <!-- Interactive Dashboard Widget -->
      <section class="dashboard-widget">
        <div class="widget-header">
          <div class="widget-title">
            <span>⚡ 核心心智與研究發現 (Interactive Insights)</span>
          </div>
          <div class="tab-nav">
            <button class="tab-btn active" data-tab="tab-strategy">🎯 戰略心智公式</button>
            <button class="tab-btn" data-tab="tab-finance">🛑 融資暫停核查</button>
            <button class="tab-btn" data-tab="tab-synergy">🌐 算力與商業協同</button>
          </div>
        </div>
        
        <div id="tab-strategy" class="tab-content active">
          <h3 style="font-size:1.3rem;color:#38bdf8;margin-bottom:1rem;">公式：Maximize P(AGI) subject to 合理利潤與團隊穩定</h3>
          <p style="color:#cbd5e1;margin-bottom:1rem;line-height:1.7;">
            與一般追求短期 ARR 極致增長的矽谷範式不同，梁文鋒公開敘事展現的一貫目標是 <strong>最大化實現 AGI 的概率</strong>。
            在這個目標函數下，「剋制」不是退縮，而是避免陷入低效資源競爭與戰線過長的生存策略：
          </p>
          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1rem;margin-top:1.5rem;">
            <div style="background:rgba(255,255,255,0.03);padding:1.2rem;border-radius:8px;border:1px solid rgba(255,255,255,0.05);">
              <h4 style="color:#f59e0b;margin-bottom:0.5rem;">🟢 開源與獲利自洽</h4>
              <p style="font-size:0.9rem;color:#94a3b8;">外傳稱十個月設備回本（payback）與口頭「六倍」口徑；分析上≠已證淨利。開源與收入無衝突是講者假設鏈，非正式財務驗證。</p>
            </div>
            <div style="background:rgba(255,255,255,0.03);padding:1.2rem;border-radius:8px;border:1px solid rgba(255,255,255,0.05);">
              <h4 style="color:#38bdf8;margin-bottom:0.5rem;">🟢 不搶 C 端芝麻</h4>
              <p style="font-size:0.9rem;color:#94a3b8;">剋制推廣，不過度消耗推理算力去爭奪低價值 C 端流量，將核心算力留給新一代架構訓練與長期探索。</p>
            </div>
            <div style="background:rgba(255,255,255,0.03);padding:1.2rem;border-radius:8px;border:1px solid rgba(255,255,255,0.05);">
              <h4 style="color:#10b981;margin-bottom:0.5rem;">🟢 AGI 階梯論</h4>
              <p style="font-size:0.9rem;color:#94a3b8;">堅持模型智能水平是根本動能，把算力投入在真正能引發能力湧現的關鍵技術節點上。</p>
            </div>
          </div>
        </div>
        
        <div id="tab-finance" class="tab-content">
          <h3 style="font-size:1.3rem;color:#f59e0b;margin-bottom:1rem;">事實層 vs 故事層：第二輪融資「暫停」內幕分離</h3>
          <p style="color:#cbd5e1;margin-bottom:1rem;line-height:1.7;">
            針對 2026-07-25 主流媒體傳言 DeepSeek 暫停第二輪融資事件，本專案嚴格依據 <code style="color:#f59e0b;">AGENTS.md</code> 進行信源核查與分離：
          </p>
          <div class="table-wrapper" style="margin-top:1rem;">
            <table class="custom-table">
              <thead>
                <tr>
                  <th>觀察維度</th>
                  <th>事實層 (Verifiable Facts)</th>
                  <th>故事層 (Speculative Narratives)</th>
                  <th>研究判定</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>停融資動作</strong></td>
                  <td>Bloomberg 單一匿名信源稱口頭暫停；Reuters 轉載且未能獨立核實。</td>
                  <td>「多家 mainstream 獨立互證」或「資金斷裂內部危機」。</td>
                  <td><span style="color:#f59e0b;font-weight:600;">Attributed／Unverified</span>（非官方、非獨立多方）。</td>
                </tr>
                <tr>
                  <td><strong>暫停原因</strong></td>
                  <td>同源報道指部分原因是首輪交流內容外傳。</td>
                  <td>「競爭對手惡意舉報」或「監管強力介入封殺」。</td>
                  <td><span style="color:#f59e0b;font-weight:600;">「惡意」未證實</span>；因果不可簡化。</td>
                </tr>
                <tr>
                  <td><strong>財務狀況</strong></td>
                  <td>外傳稱十個月設備回本（payback 口徑）；≠ 已證淨利／單位經濟。</td>
                  <td>「六倍淨利已驗證」或「將迫轉高溢價閉源」。</td>
                  <td><span style="color:#38bdf8;font-weight:600;">僅歸因於外傳</span>，不作財務蓋章。</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        
        <div id="tab-synergy" class="tab-content">
          <h3 style="font-size:1.3rem;color:#10b981;margin-bottom:1rem;">傑文斯悖論與產業正向擴散：對話 NVIDIA 與製造業降本邏輯</h3>
          <p style="color:#cbd5e1;margin-bottom:1rem;line-height:1.7;">
            評估產業串聯意見（如 StockWe 推文 2081201760669200886）：將 DeepSeek 極致架構降本與中國製造業邏輯對比，呈現出深刻的經濟學自洽：
          </p>
          <div style="background:rgba(16,185,129,0.05);border-left:4px solid #10b981;padding:1.2rem;border-radius:0 8px 8px 0;margin:1.5rem 0;">
            <p style="color:#e2e8f0;font-style:italic;margin-bottom:0.5rem;">
              "當 DeepSeek 透過算法優化（如 MLA、MoE 架構）將推理成本降低一到兩個數量級時，它並沒有摧毀算力需求，反而觸發了<strong>傑文斯悖論 (Jevons Paradox)</strong>。"
            </p>
            <p style="color:#94a3b8;font-size:0.9rem;">
              低廉的智能成本激發了前所未有的長尾調用與全行業 AI 轉型，總體算力消耗總量反而加速上升。因此，DeepSeek 的開源並非與 NVIDIA 零和博弈，反而為全球 AI 基礎設施構建了更堅實的商業協同底座。
            </p>
          </div>
        </div>
      </section>
      
      <!-- Document Archive Grid -->
      <h2 class="section-heading">📑 專案研究文獻庫 (Research Document Archive)</h2>
      <div class="card-grid">
        {cards_html}
      </div>
      
      <!-- Evidence Base Table -->
      <h2 class="section-heading">🔍 證據庫與信源矩陣 (Evidence Base Matrix)</h2>
      <div class="table-wrapper" style="margin-bottom:3.5rem;">
        <table class="custom-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>證據／來源</th>
              <th>類型</th>
              <th>支持或反對什麼</th>
              <th>可信度</th>
              <th>日期</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>S01</code></td>
              <td><a href="01_speech.html" style="color:#38bdf8;">01_speech</a> 外傳精校</td>
              <td><span style="color:#f59e0b;">Lead / Unverified</span></td>
              <td>開源、剋制、payback 等主張來源</td>
              <td>Derivative capture</td>
              <td>2026-07 外傳</td>
            </tr>
            <tr>
              <td><code>S03</code></td>
              <td>Bloomberg 匿名信源；Reuters 轉載未核實</td>
              <td><span style="color:#f59e0b;">Anonymous single-source</span></td>
              <td>口頭暫停第二輪（Attributed）</td>
              <td>非獨立互證</td>
              <td>2026-07-25</td>
            </tr>
            <tr>
              <td><code>S08</code></td>
              <td>NVIDIA 官方 SK partnership</td>
              <td><span style="color:#10b981;">Official</span></td>
              <td>&gt;$500B 級 LOI／HBM／2GW 敘事</td>
              <td>Independent official</td>
              <td>2026-07</td>
            </tr>
            <tr>
              <td><code>S02–S07/S09–S10</code></td>
              <td>本專案分析／觀點／統合</td>
              <td><span style="color:#38bdf8;">Analysis / Hypothesis</span></td>
              <td>拆解、核查、兩隊框架（見 README）</td>
              <td>不升級底層來源</td>
              <td>2026-07～08</td>
            </tr>
          </tbody>
        </table>
      </div>
      
    </main>
    
    {footer}
  </div>
  
  <script src="script.js"></script>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_content)
    print("✓ Successfully generated index.html")

def md_link_to_html(raw_text: str) -> str:
    """Rewrite local .md links to generated .html; leave external URLs alone."""

    def repl(m):
        target = m.group(1)
        anchor = m.group(2) or ""
        # reviews/02_critic_review.md → 02_critic_review.html (flat output)
        base = os.path.basename(target)
        if base.endswith(".md"):
            base = base[:-3] + ".html"
        # Map known nested paths to DOCS html names
        for doc in DOCS:
            if doc["file"] == target or doc["file"].endswith("/" + os.path.basename(target)):
                return f'({doc["html"]}{anchor})'
            if os.path.basename(doc["file"]) == os.path.basename(target):
                return f'({doc["html"]}{anchor})'
        return f'({base}{anchor})'

    return re.sub(
        r'\((\.?/?[\w\-_\./\u4e00-\u9fa5]+)\.md(#[\w\-_\.]*)?\)',
        repl,
        raw_text,
    )


def build_docs():
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc', 'nl2br'])
    missing = []

    for doc in DOCS:
        md_file = doc["file"]
        html_file = doc["html"]
        if not os.path.exists(md_file):
            missing.append(md_file)
            print(f"✗ ERROR: source missing: {md_file}")
            continue

        with open(md_file, "r", encoding="utf-8") as f:
            raw_text = f.read()

        converted_text = md_link_to_html(raw_text)

        md.reset()
        html_body = md.convert(converted_text)

        toc_items = ""
        header_idx = 0

        def replace_header(match):
            nonlocal header_idx, toc_items
            tag = match.group(1)
            content = match.group(2)
            clean_text = re.sub(r'<[^>]+>', '', content).strip()
            h_id = f"h-{header_idx}-" + re.sub(r'[^\w\u4e00-\u9fa5]', '', clean_text)[:20]
            header_idx += 1

            indent = "0" if tag == 'h1' else ("12px" if tag == 'h2' else "24px")
            toc_items += f'<li><a href="#{h_id}" class="sidebar-link" style="margin-left: {indent};">{clean_text}</a></li>\n'
            return f'<{tag} id="{h_id}">{content}</{tag}>'

        updated_html_body = re.sub(r'<(h[123])>(.*?)</\1>', replace_header, html_body, flags=re.DOTALL)

        other_docs_html = ""
        for od in DOCS:
            if od["html"] != html_file:
                other_docs_html += f'<li><a href="{od["html"]}" class="sidebar-link" style="color:#38bdf8;">📄 {od["short_title"]}</a></li>\n'

        navbar = render_navbar(html_file)
        footer = render_footer()

        page_html = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{doc['title']} · DeepSeek Research Portal</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="bg-orbs">
    <div class="orb orb-1" style="opacity: 0.1;"></div>
    <div class="orb orb-2" style="opacity: 0.1;"></div>
  </div>
  
  <div class="app-container">
    {navbar}
    
    <main class="main-content">
      <div style="margin-bottom: 1.5rem;">
        <a href="index.html" style="color:var(--text-secondary);text-decoration:none;font-size:0.9rem;">← 返回研究導航首頁</a>
      </div>
      
      <div class="doc-layout">
        <aside class="sidebar">
          <div class="sidebar-title">📑 本文目錄導覽</div>
          <ul class="sidebar-nav" style="margin-bottom: 2rem;">
            {toc_items}
          </ul>
          
          <div class="sidebar-title">📁 其他相關報告</div>
          <ul class="sidebar-nav">
            {other_docs_html}
          </ul>
        </aside>
        
        <article class="markdown-body">
          {updated_html_body}
        </article>
      </div>
    </main>
    
    {footer}
  </div>
  
  <script src="script.js"></script>
</body>
</html>"""
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"✓ Successfully generated {html_file}")

    if missing:
        raise SystemExit(f"Build failed: {len(missing)} source file(s) missing: {missing}")


def clean_orphan_html():
    expected = {d["html"] for d in DOCS} | {"index.html"}
    for name in ORPHAN_HTML_CANDIDATES:
        if name not in expected and os.path.exists(name):
            os.remove(name)
            print(f"🗑 Removed orphan HTML: {name}")


if __name__ == "__main__":
    print("🚀 Starting HTML generation for DeepSeek Research Portal...")
    build_index()
    build_docs()
    clean_orphan_html()
    print("🎉 All HTML site files generated successfully!")
