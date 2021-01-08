
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