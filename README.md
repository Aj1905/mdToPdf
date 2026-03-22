# mdToPdf

Markdown から PDF を生成する就活文書ツール。
Claude API による自動整形 + ブラウザプレビュー + PDF生成。

## セットアップ

```bash
# 依存ツール
brew install pandoc
pip install weasyprint anthropic

# API キー設定
export ANTHROPIC_API_KEY='your-api-key'
```

## 使い方

### 手動で書いた Markdown → PDF（従来通り）

```bash
make pdf                     # resume-template.md → PDF
make pdf MD=my-document.md   # 任意の .md → PDF
```

### AI 自動生成（プレビュー → 手直し → PDF）

```bash
# 履歴書
make resume USER=AJ COMPANY=Google ROLE=SWE

# スキルシート
make skillsheet USER=AJ COMPANY=Google ROLE=SWE

# エントリーシート
make entry USER=AJ COMPANY=Google ROLE=SWE
```

ブラウザが開き、プレビュー画面で内容を確認・編集。
「PDF生成」ボタンを押すと `output/` に PDF が出力される。

### 既存の生成済み Markdown を再編集

```bash
make edit USER=AJ COMPANY=Google ROLE=SWE TYPE=resume
```

## ファイル構成

```
user/        - ユーザー情報（個人ごとにフォルダを作成）
  Jun Akita/
    Jun Akita.md   - 基本情報・自己紹介・人生遍歴
    education.md   - 学歴・学業成果
    work.md        - 職歴・インターン・アルバイト
    projects.md    - 個人/チームプロジェクト
    skills.md      - 技術スキル・資格・語学
    activities.md  - 課外活動・ボランティア・リーダー経験
company/     - 企業情報（企業ごとにフォルダを作成）
  Google/
    Google.md    - 会社概要（企業文化・採用方針など）
    Intern.md    - インターン職の役割・要件
    SWE.md       - ソフトウェアエンジニア職の役割・要件
    ...          - 役職ごとにファイルを追加
job_role/    - 職種の一般情報（求められるスキル）
templates/   - 文書テンプレート（履歴書・スキルシート・ES）
output/      - 生成された Markdown / PDF
```
