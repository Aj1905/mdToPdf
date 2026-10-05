# mdToPdf - Markdown → PDF 文書生成ツール
# 必要: pandoc, weasyprint, python3, anthropic (pip install anthropic)

.PHONY: help pdf pdf-latex clean

help:
	@echo ""
	@echo "=== 手動 Markdown → PDF ==="
	@echo "  make pdf              - resume-template.md から PDF を生成"
	@echo "  make pdf MD=file.md   - 任意の .md ファイルから PDF を生成"
	@echo ""
	@echo "=== AI 自動生成 ==="
	@echo "  make resume     USER=\"Jun Akita\" COMPANY=Google   - 履歴書を生成"
	@echo "  make skillsheet USER=\"Jun Akita\" COMPANY=Google   - スキルシートを生成"
	@echo "  make entry      USER=\"Jun Akita\" COMPANY=Google   - エントリーシートを生成"
	@echo ""
	@echo "=== オプション ==="
	@echo "  make edit USER=\"Jun Akita\" COMPANY=Google TYPE=resume  - 既存MDを再編集"
	@echo ""
	@echo "=== 直接編集 ==="
	@echo "  make preview MD=file.md            - 任意のMDをプレビュー・編集"
	@echo "  make preview MD=file.md PDF=out.pdf - PDF出力先を指定"
	@echo ""

# --- 手動 PDF 生成（既存機能） ---
MD  ?= resume-template.md
PDF  = $(MD:.md=.pdf)
HTML = .resume-pandoc.html

pdf:
	pandoc $(MD) -o $(HTML) -s --metadata title="職務経歴書"
	weasyprint $(HTML) $(PDF)
	@rm -f $(HTML)
	@echo "Generated: $(PDF)"

pdf-latex:
	pandoc $(MD) -o $(PDF)

# --- AI 自動生成 ---
PYTHON  = .venv/bin/python3
USER    ?= Jun Akita
COMPANY ?= Google

resume:
	$(PYTHON) generate.py "$(USER)" "$(COMPANY)" --type resume

skillsheet:
	$(PYTHON) generate.py "$(USER)" "$(COMPANY)" --type skillsheet

entry:
	$(PYTHON) generate.py "$(USER)" "$(COMPANY)" --type entry

edit:
	$(PYTHON) generate.py "$(USER)" "$(COMPANY)" --type $(TYPE) --no-ai

preview:
	$(PYTHON) generate.py --file $(MD) $(if $(PDF),--pdf $(PDF),)

clean:
	rm -f $(HTML)
	rm -f output/*.tmp.html
