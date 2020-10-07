
NAME:=wot-classification-poc_node-red_1
DATA:=${PWD}/.node-red

# 	docker run -it -p 1880:1880 -v ${PWD}/.node-red:/data --name ${NAME} nodered/node-red

update:
	docker pull nodered/node-red
	${MAKE} stop || true
	${MAKE} run

	# --network host 
run:
	docker run --rm -d \
	-p 1880:1880 \
	-p 1881:1881 \
	-v ${DATA}:/data --name ${NAME} nodered/node-red

stop:
	docker stop ${NAME}

restart:
	docker restart ${NAME}

setup:
	sudo chown -R 1000:1000 ${DATA}

logs:
	docker logs -f ${NAME}

bash:
	docker exec -it ${NAME} /bin/bash
