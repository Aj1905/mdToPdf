# 職務経歴書 Markdown → PDF
# 必要: pandoc (https://pandoc.org/) と weasyprint (https://weasyprint.org/)
# 日本語対応のため pandoc → HTML → weasyprint で PDF 生成

MD   = resume-template.md
PDF  = resume-template.pdf
HTML = .resume-pandoc.html

.PHONY: pdf pdf-latex help clean

help:
	@echo "  make pdf       - PDFを生成 (weasyprint 使用・日本語対応)"
	@echo "  make pdf-latex - PDFを生成 (LaTeX 使用・英語向け)"
	@echo "  make clean     - 中間ファイルを削除"

pdf:
	pandoc $(MD) -o $(HTML) -s --metadata title="職務経歴書"
	weasyprint $(HTML) $(PDF)
	@rm -f $(HTML)

# LaTeX エンジン（日本語非対応）
pdf-latex:
	pandoc $(MD) -o $(PDF)

clean:
	rm -f $(HTML)
