
setup:
	virtualenv venv
	. ./venv/bin/activate && pip install -r requirements.txt

docker-build:
	docker build -t wot-docker-image .

docker-run:
	docker run --rm -p 8888:8888 wot-docker-image 

get-webthing-python:
	git clone git@gits-15.sys.kth.se:marbir/webthing-python.git

requirements:
	. ./venv/bin/activate && pip freeze > requirements.txt

run:
	. ./venv/bin/activate && python main.py
