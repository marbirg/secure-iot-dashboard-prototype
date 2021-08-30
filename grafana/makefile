
NAME:=grafana
ID:=1000

# run:
# 	docker run --rm --user ${ID} \
# 	-p 3000:3000 --name ${NAME} \
# 	-v ${PWD}/storage:/var/lib/grafana \
# 	--add-host=host.docker.internal:host-gateway \
# 	grafana/grafana

run:
	docker run --user \
	-p 3000:3000 \
	--name=${NAME} \
	-e "GF_INSTALL_PLUGINS=marcusolsson-json-datasource" \
	grafana/grafana

restart:
	docker restart ${NAME}

stop:
	docker stop ${NAME}

logs:
	docker logs -f ${NAME}


bash:
	docker exec -it ${NAME} /bin/bash
