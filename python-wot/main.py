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


def run_server():
    # Create a thing that represents a dimmable light
    # light = ExampleDimmableLight()

    # Create a thing that represents a humidity sensor
    # sensor = FakeGpioHumiditySensor()

    # Create Cab Companies:
    # patientA = CabCompany('PatientA', nCars=2)

    # Create DLM:
    label1 = DLM()

    pulseSensor = FakePulseSensor()

    sensors = [pulseSensor]
    # If adding more than one thing, use MultipleThings() with a name.
    # In the single thing case, the thing's name will be broadcast.
    server = WebThingServer(MultipleThings(sensors,
                                           'Thermometers'),
                            hostname='wot', port=8888, debug=True)
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
