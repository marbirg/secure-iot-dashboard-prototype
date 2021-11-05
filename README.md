## Introduction
This repository contains a prototype IoT system to demonstrate how to create a secure multi–user dashboard powered by a middleware and mocked IoT-devices implemented with the open source framework Web of Things.

This prototype has been created to emphasise the concepts presented in the paper ''Security-Aware Multi-User Architecture for IoT''. It contains mocked devices that should emulate pulse sensors and position sensors. The devices are implemented in Python using an open-source implementation of the Web of Things.
The middleware is implemented in Node-RED which uses a mongoDb database to store the latest fetched state for the devices and exposing them to the dashboard.

The dashboard is implemented in Graphana and shows per user different views depending on the access level of the user.

### Disclamer
This is a prototype to demonstrate the concepts from the above mentioned paper and does not have any real authorization service connected. That includes key mangement and the access keys are hence hard coded in the middleware and needs to be explicitly added in the query of the dashboard.

### Concept
The consept that this prototype demonstrate is how one can use the decentralized label model for access control in a multi-user setting with aggregated data without leakage of information to unauthorized parties.
The middleware present api:s for extracting data that has not been processed (raw data) for authorized users, as well as functions that compute over data and returns the response. On top of that functionality to declassify data according to a declassification policy is demonstrated, where the permissions from the users has been hard coded. These two main api:s demonstrate secure access by the means of filtering functions that makes sure that the functions that compute over the data only handles data that the requester has permission to access, and can by that mean avoid leakage of data.


  ## Installation
  The project is handled using Docker-compose and publicly available docker image for NodeRed. In addition a custom built image for the Web of Things endpoint, based on the open source project https://github.com/webofthings/webofthings.js

  ### Requirements:
  * docker-compose

  ## Start
  To start the project run ``make run`` or ``docker-compose up -d``.
  If this is the first time you run the project, nessecary images might need to be pulled. You can monitor the progress by looking at the logs by running ``make logs`` or ``docker-compose logs -f``.
  When everything is up and running you should be able to reach the web interfaces on the following ports:
  * Web of Things: ``http://localhost:9001`` (Patient A)
  * Web of Things: ``http://localhost:9002`` (Patient B)
  * NodeRed: ``http://localhost:1880``

  If these ports are already used on your system, you need to change the mapping in ``docker-compose.yml``
  
  ## Web of Things endpoint
  The Web of things endpoint should be available on 'http://localhost:<PORT>' where '<PORT>' is either defined in docker-compose.yml depending on what patient to which you want to connect.
  
  ## NodeRed - Middleware
  The NodeRed middleware should be available on 'http://localhost:1880'

  user:password=admin:nodered
  user:password=guest:guest

  ### Securing Node-RED:
  Source: https://nodered.org/docs/user-guide/runtime/securing-node-red#editor--admin-api-security
  Edit settings.js -> adminAuth
  Generate hash: ``node -e "console.log(require('bcryptjs').hashSync(process.argv[1], 8));" your-password-here``
  (run in nodered docker in /data directory)

## Mongo DB:
Node red needs the data base to use a pasword.
To set a password run:
use <database>
db.createUser({user:"nodered", pwd:"nodered", roles:[{role:"readWrite", db:"test"}]})
db.createUser({user:"nodered", pwd:"nodered", roles:[{role:"readWrite", db:"hospital"}]})
Source: https://docs.mongodb.com/manual/tutorial/create-users/#username-password-authentication

Update user:
db.updateUser("nodered", {roles:[{role:"readWrite", db:"hospital"},{role:"readWrite", db:"test"}]}) 
To enter mongo cli:
make mongo_bash
mongo -u root -p example
