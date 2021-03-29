
setup-thingsboard:
	mkdir -p ${PWD}/thingsboard/.mytb-data && \
	sudo chown -R 799:799 ${PWD}/thingsboard/.mytb-data
	mkdir -p ${PWD}/thingsboard/.mytb-logs && \
	sudo chown -R 799:799 ${PWD}/thingsboard/.mytb-logs

remove-thingsboard-container:
	docker rm wot-classification-poc_thingsboard_1

setup-nodered:
	sudo chown -R 1000:1000 ${PWD}/node-red/.node-red

reset-thingsboard:
	sudo rm -rf ${PWD}/thingsboard/.mytb-data
	sudo rm -rf	${PWD}/thingsboard/.mytb-logs

run:
	docker-compose up -d

build-run:
	docker-compose up -d --build

restart:
	docker-compose restart

stop:
	docker-compose down

logs:
	docker-compose logs -f --tail 50

node-red_bash:
	docker-compose exec node-red /bin/bash

mongo_bash:
	docker-compose exec mongo /bin/bash

wot_logs:
	docker logs -f wot-poc_wot_1

node-red_logs:
	docker logs -f wot-classification-poc_node-red_1

thingsboard_logs:
	docker logs -f wot-classification-poc_thingsboard_1

show-used-ports:
	sudo lsof -i -P -n | grep LISTEN
