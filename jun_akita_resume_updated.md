<style>
@page { size: A4; margin: 6mm 8mm; }
* { box-sizing: border-box; }
html { background-color: white !important; }
html, body { margin: 0 !important; padding: 0 !important; }
body { font-size: 8.5pt !important; line-height: 1.35 !important; font-family: "Hiragino Sans", "Noto Sans CJK JP", sans-serif !important; color: #222 !important; max-width: none !important; }
p { margin: 0.4mm 0 !important; }
h1, h2, h3, h4, h5, h6 { margin-top: 0 !important; }
ol, ul { margin-top: 0 !important; padding-left: 4mm !important; }
a { color: inherit !important; }

/* ── Header ── */
.header { margin-bottom: 1.5mm; }
h1 { font-size: 18pt; margin: 0 0 0.8mm; letter-spacing: 0.5pt; }
.subtitle { font-size: 10pt; color: #444; margin-bottom: 0.6mm; }
.contact { font-size: 8.5pt; color: #444; }
.contact a { color: #1a4e7c; text-decoration: none; }
.sep { margin: 0 1.5mm; color: #bbb; }
hr.divider { margin: 1.5mm 0; border: none; border-top: 0.7pt solid #999; }

/* ── Main 2-column ── */
.main { display: flex; gap: 7mm; width: 100%; }
.left-col { width: 50mm; flex-shrink: 0; }
.right-col { flex: 1; min-width: 0; }

/* ── Timeline ── */
.section-title { font-size: 9.5pt; font-weight: bold; border-bottom: 0.5pt solid #555; padding-bottom: 0.5mm; margin: 0 0 2mm; text-transform: uppercase; letter-spacing: 0.3pt; }
.tl-line { position: relative; padding-left: 4mm; }
.tl-line::before { content: ""; position: absolute; left: 1mm; top: 0; bottom: 0; width: 0.4pt; background: #ccc; }
.tl-item { position: relative; margin-bottom: 1.2mm; }
.tl-dot { position: absolute; left: -3.2mm; top: 2pt; width: 3pt; height: 3pt; border-radius: 50%; background: #555; }
.tl-date { font-size: 8pt; color: #777; }
.tl-org { font-weight: bold; font-size: 9pt; color: #1a4e7c; }
.tl-role { font-size: 8.5pt; color: #444; }
.tl-tech { font-size: 7.5pt; color: #888; margin-top: 0.2mm; }

/* ── Right col ── */
h2 { font-size: 10pt; margin: 0 0 1mm; border-bottom: 0.5pt solid #555; padding-bottom: 0.5mm; text-transform: uppercase; letter-spacing: 0.3pt; }
.item-head { display: flex; justify-content: space-between; align-items: baseline; margin: 1.5mm 0 0.4mm; }
.item-title { font-weight: bold; font-size: 9.5pt; }
.item-meta { font-size: 8.5pt; color: #666; white-space: nowrap; margin-left: 2mm; }
ul { margin: 0.3mm 0 0.6mm 0; padding-left: 4mm; list-style: disc; }
li { margin: 0.3mm 0; }
strong { font-weight: 600; }

/* ── Footer ── */
.footer { margin-top: 2mm; border-top: 0.4pt solid #ccc; padding-top: 1.5mm; display: flex; gap: 6mm; }
.footer-block { flex: 1; }
.footer-title { font-size: 9pt; font-weight: bold; margin: 0 0 1mm; border-bottom: 0.3pt solid #bbb; padding-bottom: 0.4mm; text-transform: uppercase; letter-spacing: 0.3pt; }
.stack-box { background: #f7f7f7; border: 0.4pt solid #ddd; padding: 1.5mm 2mm; font-size: 8pt; line-height: 1.5; border-radius: 1mm; }
.other-list, .strengths-list { font-size: 8pt; margin: 0; padding-left: 4mm !important; list-style: disc; }
.other-list li, .strengths-list li { margin: 0.4mm 0; }
</style>

<div class="header">
<h1>Jun Akita</h1>
<div class="subtitle">東京大学大学院 情報理工学系研究科 自然言語処理専攻</div>
<div class="contact"><strong>Email:</strong> <a href="mailto:jun.akita57@gmail.com">jun.akita57@gmail.com</a> <span class="sep">|</span> <strong>Phone:</strong> 080-5614-7439 <span class="sep">|</span> <strong>GitHub:</strong> <a href="https://github.com/Aj1905">Aj1905</a><br><strong>Portfolio:</strong> <a href="https://c46b3c12.myhomepage-1xu.pages.dev/">https://c46b3c12.myhomepage-1xu.pages.dev/</a></div>
</div>

<hr class="divider">

<div class="main">

<div class="left-col">
<div class="section-title">Timeline</div>
<div class="tl-line">

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2022/12 – 2023/04</div>
<div class="tl-org">個人開発</div>
<div class="tl-role">FX自動売買ツール</div>
<div class="tl-tech">MQL4 / MQL5 / MetaTrader</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2022/12 – 2024/07</div>
<div class="tl-org">株式会社 stardy</div>
<div class="tl-role">業務委託: 業務自動化ツール開発</div>
<div class="tl-tech">GAS / Google Forms / Spreadsheet / Python</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2023/04 – 2024/04</div>
<div class="tl-org">学生団体 Nagare</div>
<div class="tl-role">共同設立: 農家向け HP 制作</div>
<div class="tl-tech">WordPress / HTML / CSS / JavaScript</div>
</div>


<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2024/10 –</div>
<div class="tl-org">Outlier</div>
<div class="tl-role">AIモデル アノテーション</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2024/12 – 2025/01</div>
<div class="tl-org">株式会社 stardy</div>
<div class="tl-role">Discord チャットボット</div>
<div class="tl-tech">Python / GCP / Discord API</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2025/01 – 現在</div>
<div class="tl-org">ALANSE 株式会社</div>
<div class="tl-role">業務委託: AIエンジニア</div>
<div class="tl-tech">Python / LightGBM / polars / Streamlit</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2025/05 – 2025/10</div>
<div class="tl-org">合同会社 kamomemon</div>
<div class="tl-role">共同創業: プロンプト共有アプリ</div>
<div class="tl-tech">Next.js / Go / Supabase / Cloudflare</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2025/07 –</div>
<div class="tl-org">KK generation</div>
<div class="tl-role">業務委託: 画像処理 AI 開発</div>
<div class="tl-tech">TypeScript / React / Konva</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2025/11 –</div>
<div class="tl-org">Lean mathlib (OSS)</div>
<div class="tl-role">n単体のチェバの定理の逆をコントリビュート</div>
<div class="tl-tech">Lean4 / mathlib4</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-date">2026/02 –</div>
<div class="tl-org">nocall 株式会社</div>
<div class="tl-role">インターン、営業電話自動化アプリのTTSモデル開発</div>
</div>

</div>
</div>

<div class="right-col">
<h2>Selected Experience</h2>

<div class="item-head"><span class="item-title">ALANSE株式会社 — AIエンジニア</span><span class="item-meta">2025/06 – 2025/09</span></div>

- 顧客3名を含む5名体制の需要予測案件に、要件定義後の段階から参画。HUB / KIRIN CITY向けに、設計、データクリーニング、特徴量設計、モデル構築、評価、顧客説明まで担当した。
- データ量3年分・CPU運用の現実性を踏まえ、LightGBMを第一候補に設定。精度不足の場合は深層学習系へ切り替える前提で比較方針を設計し、主指標WAPE、補助指標R²で評価設計を行った。
- 当初要件の1時間単位予測ではWAPE 45%・R² 0.56と低迷。会計時刻ベース集計によるノイズが原因と分析した。
- 最終用途がシフト管理である以上1時間単位は過剰仕様と判断し、モーニング/ランチ/ディナー等の時間ブロック予測への要件変更を提案、全員の合意を形成した。
- 方針変更後に特徴量を再設計し、**WAPE 9%・R² 0.91**を達成。顧客説明ではWAPEを需要総量に対する外し率として提示し、現場判断に接続した。
- <strong>Tech:</strong> Python / LightGBM / pandas / NumPy / polars / matplotlib / Streamlit / Google Colab

<div class="item-head"><span class="item-title">サークル(天文同好会) — 副幹事長</span><span class="item-meta">学部時代 / 300人規模</span></div>

- 300人規模のサークルで副幹事長を務め、イベント・合宿の企画・準備・予約・告知など運営実務を担当した。定期イベント参加者を50人増やす目標を掲げたが、実際に増やせたのは約10人にとどまり、引退まで目標を達成できなかった。
- 事務作業や既存参加者とのコミュニケーションには取り組んでいた一方、参加率の低い層に直接アプローチする働きかけが不足していた。振り返ると、個人や少人数で完結する取り組みやすいタスクに逃げていたと感じている。
- この経験でリーダーシップの本質に気づいた。単に指示を出すのではなく、相手に寄り添いながら巻き込む実践こそがリーダーシップだと腹落ちした。また、リーダーシップとフォロワーシップは対立するものではなく、チームの状況に応じて柔軟に入れ替わる役割だと捉えている。今後は、固定された役割に縛られず、互いに支え合えるチームづくりを実践していきたい。

<h2>Other Projects</h2>
<ul>
<li><strong>Nagare / Web制作:</strong> 農家向け HP (WordPress)</li>
<li><strong>stardy / 業務自動化:</strong> GAS + Forms + Spreadsheet + GCP + Discord</li>
<li><strong>kamomemon / Webアプリ:</strong> Next.js, Go, REST API, Supabase, Cloudflare</li>
<li><strong>KK generation / 建築図面解析:</strong> TypeScript, React, Konva</li>
<li><strong>FX自動売買:</strong> MQL4, MQL5, MetaTrader4/5</li>
<li><strong>Lean mathlib / OSS:</strong> Lean4, mathlib4 — n単体のチェバの定理の逆</li>
</ul>

</div>
</div>

<div class="footer">
<div class="footer-block">
<div class="footer-title">Core Stack</div>
<div class="stack-box">Python / LightGBM / pandas / NumPy / polars / GAS / Next.js / Go / TypeScript / React / WordPress / Lean4 / MQL4 / MQL5 / GCP / Supabase / Streamlit</div>
</div>
<div class="footer-block">
<div class="footer-title">Strengths</div>
<ul class="strengths-list">
<li>要件と実運用をつなげ、粒度・評価指標まで含めた設計の見直し</li>
<li>顧客説明・合意形成まで含め、技術を業務に落とし込む力</li>
<li>数学的視点でプログラムを眺え、本質から問題にアプローチする力</li>
</ul>
</div>
</div>
