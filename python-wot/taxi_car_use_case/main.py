from __future__ import division, print_function
import os
import json

from webthing import (Action, Event, Property, MultipleThings, Thing, Value,
                      WebThingServer)
# from things.mock_DimmableLight import MockDimmableLight
# from things.mock_MovementSensor import FakeMovementSensor
from things.mock_PositionDevice import FakePositionDevice
from security.dlm import DLM

# from taxi_cab_lib import *    
# from things.mock_PositionDevice import FakePositionDevice

import logging
import random
import time
import tornado.ioloop
import uuid


DEFAULT_CONF = {
    "owner":"taxi_company",
    "readers":["taxi_company"]
}
CONFIG_FILE = os.getenv("CONFIG_FILE", "config.json")

NAME = os.getenv("FRIENDLY_NAME","taxi-car")
def readConfig(fname):
    try:
        with open(fname) as json_data_file:
            data = json.load(json_data_file)
        return data
    except Exception as e:
        print("ERROR:",e)
        return DEFAULT_CONF

def run_server():
    # Import config
    data = readConfig(CONFIG_FILE)
    policy_owner = data['owner']
    readers = data['readers']

    # Create DLM:
    dlm = DLM()
    dlm.addPolicy(policy_owner, readers)

    # Create position device:
    positionDevice = FakePositionDevice(dlm, NAME)
    # companyA = CabCompany('CustomerA', nCars=2)
    # companyB = CabCompany('CustomerB', nCars=2)
    # companyC = CabCompany('CustomerC', nCars=2)

    # positionDevices=companyA.getPositionDevices() +companyB.getPositionDevices()+companyC.getPositionDevices()

    sensors = [positionDevice]
    print("Position devices:", sensors)
    
    # position1 = FakePositionDevice()

    # sensors = [t1, t2, light1, position1]
    # If adding more than one thing, use MultipleThings() with a name.
    # In the single thing case, the thing's name will be broadcast.
    endpoint_name = 'taxiposition'+str(random.randint(0,1000))
    server = WebThingServer(MultipleThings(sensors,
                                           endpoint_name),
                            hostname='wot', port=8888, debug=True)
    try:
        logging.info('starting the server')
        server.start()
    except KeyboardInterrupt:
        logging.debug('canceling the sensor update looping task')
        for sensor in sensors:
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
