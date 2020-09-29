
  ## Installation
  The project is handled using Docker-compose, publicly available docker images for NodeRed and Thingsboard. In addition a custom built image for the Web of Things endpoint, based on the open source project https://github.com/webofthings/webofthings.js

  ### Requirements:
  * docker-compose

  ### Setup
  The Thingsboard docker image needs correct folder privilleges to work correctly, to set theese up, run ``make setup-thingsboard``

  ## Start
  To start the project run ``make run`` or ``docker-compose up -d``.
  If this is the first time you run the project, nessecary images might need to be pulled. In addition, Thingsboard needs some extra time to setup its database correctly. You can monitor the progress by looking at the logs by running ``make logs`` or ``docker-compose logs -f``.
  When everything is up and running you should be able to reach the web interfaces on the following ports:
  * Web of Things: ``http://localhost:8888``
  * NodeRed: ``http://localhost:1880``
  * Thingsboard: ``http://localhost:9090``

  If these ports are already used on your system, you need to change the mapping in ``docker-compose.yml``
  
  
  ## Web of Things endpoint
  The Web of things endpoint should be available on 'http://localhost:8888'
  
  ## NodeRed - Middleware
  The NodeRed middleware should be available on 'http://localhost:1880'

  ## Thingsboard - Dashboard
  The Thingsboard dashboard should be available on http://localhost:9090

  The credentials are the default:
  https://thingsboard.io/docs/samples/demo-account/

  ### System Administrator:
  - login: sysadmin@thingsboard.org
  - password: sysadmin

  ### Tenant:
  - login: tenant@thingsboard.org
  - password: tenant

  ### Customers:
  -  Customer A login: customer@thingsboard.org or customerA@thingsboard.org.
  - Customer B login: customerB@thingsboard.org.
  - Customer C login: customerC@thingsboard.org.

  - password: customer