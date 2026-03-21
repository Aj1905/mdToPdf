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
	@echo "  make resume    USER=AJ COMPANY=Google ROLE=SWE    - 履歴書を生成"
	@echo "  make skillsheet USER=AJ COMPANY=Google ROLE=SWE  - スキルシートを生成"
	@echo "  make entry     USER=AJ COMPANY=Google ROLE=SWE   - エントリーシートを生成"
	@echo ""
	@echo "=== オプション ==="
	@echo "  make edit USER=AJ COMPANY=Google ROLE=SWE TYPE=resume  - 既存MDを再編集"
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
USER    ?= AJ
COMPANY ?= Google
ROLE    ?= SWE

resume:
	$(PYTHON) generate.py $(USER) $(COMPANY) $(ROLE) --type resume

skillsheet:
	$(PYTHON) generate.py $(USER) $(COMPANY) $(ROLE) --type skillsheet

entry:
	$(PYTHON) generate.py $(USER) $(COMPANY) $(ROLE) --type entry

edit:
	$(PYTHON) generate.py $(USER) $(COMPANY) $(ROLE) --type $(TYPE) --no-ai

clean:
	rm -f $(HTML)
	rm -f output/*.tmp.html
