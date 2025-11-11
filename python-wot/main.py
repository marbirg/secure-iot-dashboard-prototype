from __future__ import division, print_function

from webthing import (Action, Event, Property, MultipleThings, Thing, Value,
                      WebThingServer)

from things.mock_DimmableLight import MockDimmableLight
from things.mock_MovementSensor import FakeMovementSensor
from things.mock_PositionDevice import FakePositionDevice

from things.mock_PulseSensor import FakePulseSensor

# from taxi_cab_lib import *
from security.dlm import DLM

import logging
import random
import time
import tornado.ioloop
import uuid

import json
import os

DEFAULT_CONF = {
    "name":"patient",
    "readers":["patient"]
}
CONFIG_FILE = os.getenv("CONFIG_FILE", "config.json")
def readConfig(fname):
    try:
        with open(fname) as json_data_file:
            data = json.load(json_data_file)
        return data
    except Exception as e:
        print("ERROR:",e)
        return DEFAULT_CONF

def run_server():
    data = readConfig(CONFIG_FILE)
    name = data['name']
    readers = data['readers']
    # Create DLM:
    dlm = DLM()
    dlm.addPolicy(name, readers)
    pulseSensor = FakePulseSensor(classification=dlm)

    sensors = [pulseSensor]
    # If adding more than one thing, use MultipleThings() with a name.
    # In the single thing case, the thing's name will be broadcast.
    hostname = 'wot'#+str(random.randint(0,1000))
    endpoint_name = 'pulsesensor'+str(random.randint(0,1000))
    # print("Hostname:",hostname)
    server = WebThingServer(MultipleThings(sensors,endpoint_name),
                            hostname=hostname, port=8888, debug=True)
    try:
        logging.info('starting the server')
        server.start()
    except KeyboardInterrupt:
        logging.debug('canceling the sensor update looping task')
        sensor.cancel_update_level_task()
        logging.info('stopping the server')
        server.stop()
        logging.info('done')


if __name__ == '__main__':
    logging.basicConfig(
        level=10,
        format="%(asctime)s %(filename)s:%(lineno)s %(levelname)s %(message)s"
    )
    run_server()
