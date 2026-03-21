#!/usr/bin/env python3
"""
mdToPdf - テンプレートベースの文書生成ツール
履歴書・スキルシート・エントリーシートをAIで自動整形し、PDF化する。

使い方:
  python generate.py <user> <company> <job_role> --type resume
  python generate.py AJ Google SWE --type skillsheet
  python generate.py AJ Google SWE --type entry

フロー:
  1. user/company/job_role の情報を読み込み
  2. テンプレートに沿って Claude API が文章を整形・生成
  3. Markdown を保存 → ブラウザでプレビュー表示（編集可能）
  4. ブラウザ上の「PDF生成」ボタンを押して PDF 出力
"""

import argparse
import http.server
import json
import os
import subprocess
import sys
import threading
import urllib.parse
import webbrowser
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

try:
    import anthropic
except ImportError:
    print("Error: anthropic パッケージが必要です。")
    print("  pip install anthropic")
    sys.exit(1)


BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
OUTPUT_DIR = BASE_DIR / "output"

DOC_TYPES = {
    "resume": {"name": "履歴書", "template": "resume-template.md", "template_dir": BASE_DIR},
    "skillsheet": {"name": "スキルシート", "template": "skillsheet.md", "template_dir": TEMPLATES_DIR},
    "entry": {"name": "エントリーシート", "template": "entry.md", "template_dir": TEMPLATES_DIR},
}


def read_file(path: Path) -> str:
    if not path.exists():
        print(f"Error: ファイルが見つかりません: {path}")
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def build_prompt(user_info: str, company_info: str, job_role_info: str,
                 template: str, doc_type_name: str) -> str:
    return f"""あなたは日本語の就職活動文書を作成する専門家です。

以下の情報を元に、テンプレートの形式に沿って「{doc_type_name}」を作成してください。

## 指示
- テンプレートの各セクション（{{...}}のプレースホルダー）を適切な内容で埋めてください
- ユーザーの経歴・スキルを、応募先企業と職種に最適化して整形してください
- 文章は簡潔かつプロフェッショナルに、日本語の就活文書として自然な表現にしてください
- 事実に基づいて書き、情報を捏造しないでください
- Markdown形式で出力してください（コードブロックで囲まないでください）
- テンプレートにあるHTMLタグ（imgタグなど）はそのまま残してください

## ユーザー情報
{user_info}

## 応募先企業情報
{company_info}

## 職種情報
{job_role_info}

## テンプレート
{template}

上記テンプレートのプレースホルダーを埋めた完成版のMarkdownを出力してください。"""


def generate_with_ai(prompt: str) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY 環境変数を設定してください。")
        print("  export ANTHROPIC_API_KEY='your-api-key'")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print("AIが文書を生成中...")
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def md_to_html_body(md_content: str) -> str:
    """pandoc で Markdown → HTML body 変換"""
    result = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html"],
        input=md_content, capture_output=True, text=True,
    )
    if result.returncode != 0:
        return f"<pre>{md_content}</pre>"
    return result.stdout


def generate_pdf(md_path: Path, pdf_path: Path) -> bool:
    """Markdown → HTML → PDF (weasyprint)"""
    html_tmp = md_path.with_suffix(".tmp.html")
    try:
        result = subprocess.run(
            ["pandoc", str(md_path), "-o", str(html_tmp), "-s",
             "--metadata", "title=文書"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return False

        result = subprocess.run(
            ["weasyprint", str(html_tmp), str(pdf_path)],
            capture_output=True, text=True,
        )
        return result.returncode == 0
    finally:
        if html_tmp.exists():
            html_tmp.unlink()


def build_preview_html(md_content: str, md_path: Path) -> str:
    """プレビュー用 HTML（編集エリア + PDF生成ボタン付き）"""
    html_body = md_to_html_body(md_content)
    escaped_md = md_content.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>mdToPdf プレビュー</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", sans-serif; background: #f5f5f5; }}
  .toolbar {{
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    background: #1a1a2e; color: #fff; padding: 12px 24px;
    display: flex; align-items: center; gap: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  }}
  .toolbar h1 {{ font-size: 16px; font-weight: 600; }}
  .toolbar .spacer {{ flex: 1; }}
  .tab-btn {{
    padding: 6px 16px; border: 1px solid #555; border-radius: 6px;
    background: transparent; color: #ccc; cursor: pointer; font-size: 13px;
  }}
  .tab-btn.active {{ background: #e94560; border-color: #e94560; color: #fff; }}
  .btn-pdf {{
    padding: 8px 24px; border: none; border-radius: 6px;
    background: #0f3460; color: #fff; cursor: pointer;
    font-size: 14px; font-weight: 600;
  }}
  .btn-pdf:hover {{ background: #16213e; }}
  .btn-pdf:disabled {{ opacity: 0.5; cursor: not-allowed; }}
  .status {{ font-size: 12px; color: #aaa; }}
  .container {{ margin-top: 56px; display: flex; height: calc(100vh - 56px); }}
  .editor-pane {{
    width: 50%; padding: 16px; display: none;
    border-right: 1px solid #ddd; background: #fff;
  }}
  .editor-pane.active {{ display: block; }}
  .editor-pane textarea {{
    width: 100%; height: 100%; border: none; outline: none;
    font-family: "SF Mono", "Fira Code", monospace; font-size: 13px;
    line-height: 1.6; resize: none; padding: 8px;
  }}
  .preview-pane {{
    flex: 1; padding: 24px 32px; overflow-y: auto; background: #fff;
  }}
  .preview-pane.full {{ width: 100%; max-width: 800px; margin: 0 auto; }}
  .preview-pane h1 {{ font-size: 1.6em; margin: 16px 0 8px; }}
  .preview-pane h2 {{ font-size: 1.3em; margin: 16px 0 8px; border-bottom: 1px solid #eee; padding-bottom: 4px; }}
  .preview-pane h3, .preview-pane h4 {{ margin: 12px 0 6px; }}
  .preview-pane p {{ margin: 6px 0; line-height: 1.7; }}
  .preview-pane ul, .preview-pane ol {{ margin: 6px 0 6px 24px; }}
  .preview-pane table {{ border-collapse: collapse; margin: 8px 0; width: 100%; }}
  .preview-pane th, .preview-pane td {{ border: 1px solid #ddd; padding: 6px 10px; text-align: left; }}
  .preview-pane th {{ background: #f9f9f9; }}
  .preview-pane hr {{ margin: 16px 0; border: none; border-top: 1px solid #eee; }}
  .toast {{
    position: fixed; bottom: 24px; right: 24px; padding: 12px 24px;
    border-radius: 8px; color: #fff; font-size: 14px;
    display: none; z-index: 200;
  }}
  .toast.success {{ background: #2d6a4f; display: block; }}
  .toast.error {{ background: #d00; display: block; }}
</style>
</head>
<body>

<div class="toolbar">
  <h1>mdToPdf</h1>
  <div class="spacer"></div>
  <button class="tab-btn active" onclick="toggleEditor(false)">プレビュー</button>
  <button class="tab-btn" onclick="toggleEditor(true)">編集</button>
  <button class="btn-pdf" id="pdfBtn" onclick="generatePdf()">PDF生成</button>
  <span class="status" id="status"></span>
</div>

<div class="container">
  <div class="editor-pane" id="editorPane">
    <textarea id="mdEditor" spellcheck="false">{md_content}</textarea>
  </div>
  <div class="preview-pane" id="previewPane">
    {html_body}
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
let editorActive = false;
let debounceTimer = null;

function toggleEditor(show) {{
  editorActive = show;
  const btns = document.querySelectorAll('.tab-btn');
  btns[0].classList.toggle('active', !show);
  btns[1].classList.toggle('active', show);
  document.getElementById('editorPane').classList.toggle('active', show);
  document.getElementById('previewPane').classList.toggle('full', !show);
}}

// Markdown 編集時にサーバーに保存＋プレビュー更新
document.getElementById('mdEditor').addEventListener('input', function() {{
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {{
    const md = this.value;
    fetch('/save', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{markdown: md}})
    }})
    .then(r => r.json())
    .then(data => {{
      document.getElementById('previewPane').innerHTML = data.html;
    }});
  }}, 500);
}});

function generatePdf() {{
  const btn = document.getElementById('pdfBtn');
  const status = document.getElementById('status');
  btn.disabled = true;
  status.textContent = 'PDF生成中...';

  fetch('/generate-pdf', {{ method: 'POST' }})
    .then(r => r.json())
    .then(data => {{
      btn.disabled = false;
      if (data.success) {{
        status.textContent = '';
        showToast('PDF を生成しました: ' + data.path, 'success');
      }} else {{
        status.textContent = '';
        showToast('PDF 生成に失敗しました', 'error');
      }}
    }})
    .catch(() => {{
      btn.disabled = false;
      status.textContent = '';
      showToast('通信エラー', 'error');
    }});
}}

function showToast(msg, type) {{
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast ' + type;
  setTimeout(() => {{ t.className = 'toast'; }}, 4000);
}}
</script>
</body>
</html>"""


class PreviewHandler(http.server.BaseHTTPRequestHandler):
    """プレビューサーバーのリクエストハンドラ"""

    md_path = None
    pdf_path = None
    md_content = ""
    shutdown_event = None

    def log_message(self, format, *args):
        pass  # ログ抑制

    def do_GET(self):
        if self.path == "/":
            html = build_preview_html(self.__class__.md_content, self.__class__.md_path)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len).decode("utf-8")

        if self.path == "/save":
            data = json.loads(body)
            md = data["markdown"]
            self.__class__.md_content = md
            self.__class__.md_path.write_text(md, encoding="utf-8")
            html_body = md_to_html_body(md)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"html": html_body}).encode("utf-8"))

        elif self.path == "/generate-pdf":
            md_p = self.__class__.md_path
            pdf_p = self.__class__.pdf_path
            success = generate_pdf(md_p, pdf_p)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            result = {"success": success, "path": str(pdf_p)}
            self.wfile.write(json.dumps(result).encode("utf-8"))
            if success:
                print(f"\nPDF を生成しました: {pdf_p}")

        else:
            self.send_response(404)
            self.end_headers()


def start_preview_server(md_content: str, md_path: Path, pdf_path: Path,
                         port: int = 8787) -> None:
    """プレビューサーバーを起動してブラウザで開く"""
    PreviewHandler.md_path = md_path
    PreviewHandler.pdf_path = pdf_path
    PreviewHandler.md_content = md_content

    server = http.server.HTTPServer(("127.0.0.1", port), PreviewHandler)
    print(f"\nプレビューサーバー起動: http://localhost:{port}")
    print("ブラウザで編集し、「PDF生成」ボタンでPDFを出力できます。")
    print("終了するには Ctrl+C を押してください。")

    webbrowser.open(f"http://localhost:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nサーバーを終了しました。")
        server.server_close()


def main():
    parser = argparse.ArgumentParser(
        description="mdToPdf - AI文書生成ツール（履歴書・スキルシート・エントリーシート）",
    )
    parser.add_argument("user", help="ユーザー名（user/ 内のファイル名、拡張子不要）")
    parser.add_argument("company", help="企業名（company/ 内のファイル名、拡張子不要）")
    parser.add_argument("job_role", help="職種名（job_role/ 内のファイル名、拡張子不要）")
    parser.add_argument(
        "--type", "-t", dest="doc_type", default="resume",
        choices=DOC_TYPES.keys(),
        help="文書タイプ（default: resume）",
    )
    parser.add_argument(
        "--no-ai", action="store_true",
        help="AI生成をスキップし、既存のMarkdownからプレビューを開く",
    )
    parser.add_argument(
        "--port", type=int, default=8787,
        help="プレビューサーバーのポート（default: 8787）",
    )
    args = parser.parse_args()

    doc_info = DOC_TYPES[args.doc_type]
    OUTPUT_DIR.mkdir(exist_ok=True)

    # 出力ファイルパス
    output_name = f"{args.user}_{args.company}_{args.job_role}_{args.doc_type}"
    md_output = OUTPUT_DIR / f"{output_name}.md"
    pdf_output = OUTPUT_DIR / f"{output_name}.pdf"

    if args.no_ai:
        # 既存 Markdown からプレビュー
        if not md_output.exists():
            print(f"Error: Markdownファイルが見つかりません: {md_output}")
            sys.exit(1)
        generated_md = md_output.read_text(encoding="utf-8")
    else:
        # 入力ファイル読み込み
        user_info = read_file(BASE_DIR / "user" / f"{args.user}.md")
        company_info = read_file(BASE_DIR / "company" / f"{args.company}.md")
        job_role_info = read_file(BASE_DIR / "job_role" / f"{args.job_role}.md")
        template = read_file(doc_info["template_dir"] / doc_info["template"])

        # AI で文書生成
        prompt = build_prompt(user_info, company_info, job_role_info,
                              template, doc_info["name"])
        generated_md = generate_with_ai(prompt)

        # Markdown 保存
        md_output.write_text(generated_md, encoding="utf-8")
        print(f"Markdown を保存しました: {md_output}")

    # プレビューサーバー起動（ブラウザで編集 → ボタンでPDF生成）
    start_preview_server(generated_md, md_output, pdf_output, args.port)


if __name__ == "__main__":
    main()
