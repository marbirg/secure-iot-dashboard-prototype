from __future__ import division, print_function

from webthing import (Action, Event, Property, MultipleThings, Thing, Value,
                      WebThingServer)
from things.mock_DimmableLight import MockDimmableLight
from things.mock_MovementSensor import FakeMovementSensor
from things.mock_PositionDevice import FakePositionDevice

from taxi_cab_lib import *    

import logging
import random
import time
import tornado.ioloop
import uuid


class OverheatedEvent(Event):

    def __init__(self, thing, data):
        Event.__init__(self, thing, 'overheated', data=data)


class FadeAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'fade', input_=input_)

    def perform_action(self):
        time.sleep(self.input['duration'] / 1000)
        self.thing.set_property('brightness', self.input['brightness'])
        self.thing.add_event(OverheatedEvent(self.thing, 102))


class ExampleDimmableLight(Thing):
    """A dimmable light that logs received commands to stdout."""

    def __init__(self):
        Thing.__init__(
            self,
            'urn:dev:ops:my-lamp-1234',
            'My Lamp',
            ['OnOffSwitch', 'Light'],
            'A web connected lamp'
        )

        self.add_property(
            Property(self,
                     'on',
                     Value(True, lambda v: print('On-State is now', v)),
                     metadata={
                         '@type': 'OnOffProperty',
                         'title': 'On/Off',
                         'type': 'boolean',
                         'description': 'Whether the lamp is turned on',
                     }))

        self.add_property(
            Property(self,
                     'brightness',
                     Value(50, lambda v: print('Brightness is now', v)),
                     metadata={
                         '@type': 'BrightnessProperty',
                         'title': 'Brightness',
                         'type': 'integer',
                         'description': 'The level of light from 0-100',
                         'minimum': 0,
                         'maximum': 100,
                         'unit': 'percent',
                     }))

        self.add_available_action(
            'fade',
            {
                'title': 'Fade',
                'description': 'Fade the lamp to a given level',
                'input': {
                    'type': 'object',
                    'required': [
                        'brightness',
                        'duration',
                    ],
                    'properties': {
                        'brightness': {
                            'type': 'integer',
                            'minimum': 0,
                            'maximum': 100,
                            'unit': 'percent',
                        },
                        'duration': {
                            'type': 'integer',
                            'minimum': 1,
                            'unit': 'milliseconds',
                        },
                    },
                },
            },
            FadeAction)

        self.add_available_event(
            'overheated',
            {
                'description':
                'The lamp has exceeded its safe operating temperature',
                'type': 'number',
                'unit': 'degree celsius',
            })


class FakeGpioHumiditySensor(Thing):
    """A humidity sensor which updates its measurement every few seconds."""

    def __init__(self):
        Thing.__init__(
            self,
            'urn:dev:ops:my-humidity-sensor-1234',
            'My Humidity Sensor',
            ['MultiLevelSensor'],
            'A web connected humidity sensor'
        )

        self.level = Value(0.0)
        self.add_property(
            Property(self,
                     'level',
                     self.level,
                     metadata={
                         '@type': 'LevelProperty',
                         'title': 'Humidity',
                         'type': 'number',
                         'description': 'The current humidity in %',
                         'minimum': 0,
                         'maximum': 100,
                         'unit': 'percent',
                         'readOnly': True,
                     }))

        logging.debug('starting the sensor update looping task')
        self.timer = tornado.ioloop.PeriodicCallback(
            self.update_level,
            3000
        )
        self.timer.start()

    def update_level(self):
        new_level = self.read_from_gpio()
        logging.debug('setting new humidity level: %s', new_level)
        self.level.notify_of_external_update(new_level)

    def cancel_update_level_task(self):
        self.timer.stop()

    @staticmethod
    def read_from_gpio():
        """Mimic an actual sensor updating its reading every couple seconds."""
        return abs(70.0 * random.random() * (-0.5 + random.random()))

class FakeGpioThermometerSensor(Thing):
    """A humidity sensor which updates its measurement every few seconds."""
    _instance_number = 0
    _MIN_VALUE = -20
    _MAX_VALUE = 50

    
    def __init__(self, classification='private'):
        FakeGpioThermometerSensor._instance_number+=1
        self._value = 20 # Initial value
        Thing.__init__(
            self,
            'urn:dev:ops:fake-thermo-' + str(FakeGpioThermometerSensor._instance_number), #id
            'Fake thermometer', #title
            ['MultiLevelSensor'], #type
            'A web connected humidity sensor', #description
            classification = classification
        )

        self.level = Value(0.0)
        self.add_property(
            Property(self,
                     'level',
                     self.level,
                     metadata={
                         '@type': 'LevelProperty',
                         'title': 'Temperature',
                         'type': 'number',
                         'description': 'The current temperature in Celsius',
                         'minimum': FakeGpioThermometerSensor._MIN_VALUE,
                         'maximum': FakeGpioThermometerSensor._MAX_VALUE,
                         'unit': 'Celcius',
                         'readOnly': True,
                     }))

        logging.debug('starting the sensor update looping task')
        self.timer = tornado.ioloop.PeriodicCallback(
            self.update_level,
            3000
        )
        self.timer.start()

    def update_level(self):
        new_level = self.read_from_gpio()
        logging.debug('setting new temperature level: %s', new_level)
        self.level.notify_of_external_update(new_level)

    def cancel_update_level_task(self):
        self.timer.stop()

    # @staticmethod
    def read_from_gpio(self):
        """Mimic an actual sensor updating its reading every couple seconds."""
        self._value = self._value + random.random() * (-0.5 + random.random())
        # print("New gpio value:", self._value)
        return self._value
        return abs(self._last_value + random.random() * (-0.5 + random.random()))


def run_server():
    # Create a thing that represents a dimmable light
    # light = ExampleDimmableLight()

    # Create a thing that represents a humidity sensor
    # sensor = FakeGpioHumiditySensor()

    # Create Cab Companies:
    companyA = CabCompany('CustomerA', nCars=2)
    companyB = CabCompany('CustomerB', nCars=2)
    companyC = CabCompany('CustomerC', nCars=2)

    positionDevices=companyA.getPositionDevices() +companyB.getPositionDevices()+companyC.getPositionDevices()

    print("Position devices:", positionDevices)
    
    
    t1 = FakeGpioThermometerSensor(classification='private')
    t2 = FakeGpioThermometerSensor(classification='public')

    light1 = MockDimmableLight()

    position1 = FakePositionDevice()

    # sensors = [t1, t2, light1, position1]
    sensors = positionDevices
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
