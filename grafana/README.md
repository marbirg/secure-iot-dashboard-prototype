

## Grafana
Docs: https://grafana.com/docs/grafana/latest/administration/configuration/
Docker: https://grafana.com/docs/grafana/latest/administration/configure-docker/


## Credentials:
Default: admin:admin


## Plugins:

### Simple json data source plugin
To get data using REST
Documentation: https://grafana.com/grafana/plugins/grafana-simple-json-datasource

Comment: Seams to dependent on back-end implementation

#### Installation
sudo grafana-cli plugins install grafana-simple-json-datasource
sudo service grafana-server restart

### Json API

### Installation
grafana-cli plugins install marcusolsson-json-datasource