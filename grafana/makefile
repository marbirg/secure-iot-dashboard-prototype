
NAME:=grafana
ID:=1000

run:
	docker run --rm -d --user ${ID} \
	-p 3000:3000 --name ${NAME} \
	-v ${PWD}/storage:/var/lib/grafana \
	--add-host=host.docker.internal:host-gateway \
	grafana/grafana

restart:
	docker restart ${NAME}

stop:
	docker stop ${NAME}

logs:
	docker logs -f ${NAME}


bash:
	docker exec -it ${NAME} /bin/bash
