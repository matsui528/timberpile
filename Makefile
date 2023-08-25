.PHONY: all clean

all:
	python main.py --output_type md --output output.md
	python main.py --output_type html --output output.html
	python main.py --output_type bibtex --output output.bib

clean:
	rm -rf output.md output.html output.bib
