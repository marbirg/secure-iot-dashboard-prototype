

## Setup:
Run: ``make run``

Open a browser at <IP>:3000

Login with admin:admin
You will be requested to change password

Select 'Create new data source'

Choose 'JSON API'
For data for cabA1:
Use the following url: http://<IP>:2880/properties
where you change to the ip of the middleware (NodeRED)

Use the following query string:
device_id=mock:position:cabA1&@type=PositionProperty&principal=CompanyA&fetch=name,data,classification

Name it "Cab A1 position"

For the public data source, use the following query string:
Use the following url: http://<IP>:2880/declassified-dist

Name it Public cab distribution


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