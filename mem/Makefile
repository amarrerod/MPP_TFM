all:
	pdflatex memtfm.tex
	bibtex memtfm
	pdflatex memtfm.tex

html:
	pdf2htmlEX memtfm.pdf

clean:
	rm -f *.toc *.ps *.log *.lof *.lot *.dvi *.aux *.blg *.bbl
