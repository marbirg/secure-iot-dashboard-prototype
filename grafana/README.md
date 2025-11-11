

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

Import CompanyA-Dashboard-Example.json

## Grafana
Docs: https://grafana.com/docs/grafana/latest/administration/configuration/
Docker: https://grafana.com/docs/grafana/latest/administration/configure-docker/


## Credentials:
Default: admin:admin


## Plugins:

### Manual Installation

#### Json API
grafana-cli plugins install marcusolsson-json-datasource
sudo service grafana-server restart