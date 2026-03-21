# 職務経歴書

<img src="./profile.JPG" align="right" style="border-radius: 50%; width: 120px; height:160px" >

<br/>

<span style="font-size: 1.4em">AJ</span>

<br/>

## 職務要約

学部の間、AI開発・Web開発・業務自動化・需要予測・OSS貢献まで幅広く実践。  
要件整理から設計、実装、検証、顧客説明まで一貫して担当した案件を複数経験。  
特に、Google Workspace/GAS連携による業務ツール開発、LightGBMを用いた需要予測モデル構築、Lean(mathlib)への定理実装など、実務寄りの開発と理論寄りの開発の両面に強み。
大学院進学し、東京大学で自然言語処理を専攻する見込み。

## 経験・スキルセット

- 業務自動化ツール開発（Google Apps Script, Google Forms, Spreadsheet）
- 機械学習モデル構築・検証（LightGBM, 需要予測）
- 画像処理AI向けデータアノテーション（YOLOv8）
- Webアプリ開発（Next.js, Go API）
- WordPressによるサイト構築・運用
- 金融向け自動売買ツール開発（MQL4/MQL5, MT4/MT5）
- 顧客向け説明・要件調整・提案
- OSSコントリビュート（Lean mathlib）
- 建築図面解析の画像処理アルゴリズムの構築

## 職務履歴

所属 | 時期 | 役割
---------- | ----------------- | -----------------------------
株式会社stardy | 2022/12 - 2025/6 | エンジニア（従業員管理ツール、生徒対応チャットボット開発）
学生団体Nagare | 2023/06 - 2024/10 | Web担当（PRサイト制作）
株式会社ARCRA | 2025/06 - 現在 | 画像処理AIアノテーション担当
ALANSE株式会社 | 2025/01 - 現在 | AIエンジニア（需要予測）
Outlier | 2024/12 - 現在 | AIアノテーション担当
個人開発 | 2022/11 - 2022/12 | FX自動売買ツール開発
共同創業プロジェクト | 2025/06 - 2025/10 | 共同創業者（企画・開発・営業）
OSS（Lean mathlib） | 2025/11 - 現在 | Contributor（チェバの定理の形式化）
個人開発 | 2025/11 - 2025/11 | クローンアプリ開発（vibe coding）
KK-generation | 2026/1 - 2026/2 | 建築図面可視化アプリ開発

---


## 株式会社stardy(2022/12 - 2025/6)

#### 主な実績

Google WorkspaceとGASを用いた従業員管理ツールを開発。  
フォーム入力、スプレッドシート管理、スクリプト自動処理を連携し、運用効率化を支援。また生徒対応のチャットボットアプリを作成し、Discord上で運用、生徒への質問に迅速に答える仕組みを構築。
IT関連の知識の基礎を培った。

- Google Forms / Spreadsheet / GAS の連携設計

#### チーム構成

一人で実装担当として開発を実施。

#### 技術スタック

従業員管理ツール

Lang/Framefowrk/Tools | Tech Stack
--- | ---
Programing Language | JavaScript (GAS)
DataBase | Google Spreadsheet
Communication | Slack
Documentation | Notion

チャットボット

Lang/Framefowrk/Tools | Tech Stack
--- | ---
Programing Language | Python
Cloud Server | Google Cloud Platform, Glitch（サービス終了）
Communication | Discord

#### Appendix

- [株式会社stardy](https://stardy.co.jp/)

---

## ALANSE株式会社(2025/01 - 現在)

#### 主な実績

British Pub Hubおよびキリンシティ向けの需要予測AIモデルを構築。  
設計、特徴量検討、モデル構築、評価、顧客説明まで一通り担当。
顧客の要件では1時間ごとの予測モデルの構築が目標だったが、モデルの使用目的が従業員のシフト管理であったことから、ランチ・ディナーなどの時間ブロック予測の方が合理的だと提言し、その方針に変更になったとことが最も工夫した点である。
その他、HP制作業務なども担当。

- LightGBMを用いた需要予測モデルを開発
- 時間ブロック単位の予測手法を設計・実装
- 決定係数 R² 0.85〜0.90 を達成
- 顧客向け報告・説明資料作成および説明を実施

#### チーム構成

メンターと二人で、モデリング担当として設計〜説明までを主導。
初のチーム開発を経験。

#### 技術スタック

Lang/Framefowrk/Tools | Tech Stack
--- | ---
Programing Language | Python
ML | LightGBM
Data Processing | pandas, NumPy, polars
Visualization | matplotlib
Communication | Slack, Google Meet, Github
Tools | Streamlit
Documentation | Google Colab

#### Appendix

- [ALANSE株式会社](https://www.alanse.co.jp/)

---

## 学生団体Nagare(2023/06 - 2024/10)

#### 主な実績

愛知県弥富市の金魚農家（深海養魚場）の売上回復PR施策の一環としてHPを制作。
同様に、岐阜県本巣市のいちご農家（Doing）の宣伝の一環でHPを制作。

- WordPressによるサイト構築
- 情報設計、ページ制作、公開対応
- 地域PRを目的としたコンテンツ整備

#### チーム構成

友人と立ち上げた学生団体で活動。
HP作成担当として参加。

#### 技術スタック

Lang/Framefowrk/Tools | Tech Stack
--- | ---
CMS | WordPress
Tools | local
Frontend | HTML, CSS, JavaScript

#### Appendix

- [深海養魚場] https://theclubmoney.net/
- [いちご農園Doing] https://doing-ichigo.com/

---

## 株式会社ARCRA(2025/06 - 現在)

#### 主な実績

真珠の傷判定を行う画像処理AIソフト開発案件に参画。  
主にYOLOv8の学習用データアノテーションを担当。

- バウンディングボックス形式のアノテーション作業
- 学習データ整備・品質確認を支援

#### チーム構成

画像処理AI案件チームの一員として参画。

#### 技術スタック

Lang/Framefowrk/Tools | Tech Stack
--- | ---
ML | YOLOv8（Bounding Box）
Communication | Discord

#### Appendix

- [株式会社ARCRA](https://arcra.jp/)

---

## Outlier(2024/12 - 現在)

#### 主な実績

AIモデル向けのアノテーション業務およびレビュアーを担当。マニュアルに従うだけの業務だったが、自然言語処理・画像処理・音声処理アノテーションの流れを一通り経験できた。

- データラベリング
- ルールに基づく品質担保

#### チーム構成

プロジェクト単位での業務参加。

#### 技術スタック

Lang/Framefowrk/Tools | Tech Stack
--- | ---
Documentation | Outlier専用プラットフォームとマニュアル

#### Appendix

- [Outlier](https://app.outlier.ai/)

---

## 個人開発 (2022/11 - 2022/12)

#### 主な実績

MT4/MT5向けに、MQL4/MQL5でFX自動売買支援ツールを開発。

- インジケータ開発
- エキスパートアドバイザ（EA）開発
- 売買判断補助ロジックの実装

#### 技術スタック

Lang/Framefowrk/Tools | Tech Stack
--- | ---
Programing Language | MQL4, MQL5
Platform | MetaTrader4, MetaTrader5

---

## 共同創業プロジェクト(プロンプト共有プラットフォーム) (2025/06 - 2025/10)

#### 主な実績

友人と起業し、プロンプト共有プラットフォームを立ち上げ、アイデア創出、要件整理、設計、実装、営業までを一貫して担当。
AI上級者が投稿したプロンプトをその場で実行できるようにすることで、AI普及率の向上を狙った（当時普及率が5％だった）。chatGPTなどのサブスク料金が3000円前後なのに対し、このプラットフォーム上での実行はAPI料金の高々10円であるというのが強みだったが、直後に発表されたchatGPT5が無料であったため、優位性がなくなりデプロイまでは至らなかった。

開発自体は友人と二人で行った。

- プロダクト企画および要件定義
- フロントエンド実装（Next.js）
- バックエンドAPI実装（Go）
- ユーザー獲得に向けた営業活動
- 市場変化（ChatGPT無料化）に伴う競争優位の低下を受け、撤退判断

#### 技術スタック

Lang/Framefowrk/Tools | Tech Stack
--- | ---
Frontend | Next.js
Backend | Go
API | REST API
Infrastructure | supabase, cloudflare
Project Management | Notion / GitHub

---

## OSS（Lean mathlib）(2025/11 - 現在)

#### 主な実績

自動定理証明支援ツールLeanのmathlibライブラリ拡充。
n単体についての一般化チェバの定理の逆を追加中。
OSS開発の作法を経験。

- 定理実装
- 形式検証に基づくOSSコントリビュート

#### 技術スタック

Lang/Framefowrk/Tools | Tech Stack
--- | ---
Language | Lean4
Library | mathlib4
Tool | Aristotle.ai
Communication | Zulip, Discord

---

## 個人開発 (2025/11 - 2025/11)

#### 主な実績

アメリカで話題になっていたCluelyのクローンアプリを設計し、開発工程はvibe codingで実施。画面共有に映らず、タスクマネージャにも表示されないAIアプリを作成。

- 要件の簡易設計
- 実装主導でプロトタイプ化

#### 技術スタック

Lang/Framefowrk/Tools | Tech Stack
--- | ---
Framework | Electron
Development Style | vibe coding
Tool | codex

## KK-generation（2026/1 - 2026/2）

#### 主な実績

建築図面を解析し、建築に必要な情報を計算・可視化するアルゴリズムを考案。それを実装した簡易的なWebアプリを構築。
主に、建物内の壁の総面積を図面から計算するアルゴリズムを担当したが、壁がない部屋の壁面積を計算するアルゴリズムの構築を工夫した。

#### 技術スタック

Lang/Framefowrk/Tools | Tech Stack
--- | ---
Programing Language | Typescript
Frontend | React
Library | Konva

## Appendix

- [GitHub](https://github.com/Aj1905)
- [Portfolio](https://c46b3c12.myhomepage-1xu.pages.dev/)
