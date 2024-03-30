.PHONY: data, clean


data/APR_data.csv:
	mkdir -p data
	cd data; curl -LO https://ncaaorg.s3.amazonaws.com/research/academics/2020RES_APR2019PubDataShare.csv

tidy: data/APR_data.csv
	python -B src/get_tidy_data.py

plot1: tidy
	mkdir -p figs
	python -B src/question_1.py


plot2: tidy
	mkdir -p figs
	python -B src/question_2.py

plot3: tidy
	mkdir -p figs
	python -B src/question_3.py

clean:
	rm -r data
