import logging

from webthing import (Action, Event, Property, MultipleThings, Thing, Value,
                      WebThingServer)

from security.dlm import DLM

import tornado.ioloop
import random
import numpy as np

# For debug
use_static = True
static_values = {
    'urn:dev:ops:fake-position-1':1,
    'urn:dev:ops:fake-position-2':2,
    'urn:dev:ops:fake-position-3':3,
    'urn:dev:ops:fake-position-4':3,
    'urn:dev:ops:fake-position-5':2,
    'urn:dev:ops:fake-position-6':4,
}

class FakePulseSensor(Thing):
    """A sensor that detects movment."""
    _id_prefix = 'urn:dev:ops:fake-pulse-'
    _instance_number = 0
    _values = [1,2,3,4]
    
    def __init__(self, classification=None, name=None):
        type(self)._instance_number+=1
        self.device_id = FakePulseSensor._id_prefix + str(type(self)._instance_number) #id
        self.name = name if name else self.device_id
        self.classification = classification if classification else DLM()

        
        print("Create new device:", self.name,"With classification:",classification)
        # self._position_index = random.randint(0, len(FakePositionDevice._values)-1) 
        # self._position = FakePositionDevice._values[self._position_index] # Initial value
        self._value = self.getInitialValue()
        Thing.__init__(
            self,
            self.device_id,
            name, #title
            ['DiscretePostitionDevice'], #type
            'A device reporting its position', #description
            classification = classification
        )

        self.value = Value(self._value)
        self.add_property(
            Property(self,
                     'pulse',
                     self.value,
                     metadata={
                         '@type': 'PulseData',
                         'title': 'Pulse',
                         'type': 'float',
                         'description': 'Real time pulse value',
                         'readOnly': True,
                     }))

        logging.debug('starting the sensor update looping task')
        self.timer = tornado.ioloop.PeriodicCallback(
            self.update_level,
            3000
        )
        self.timer.start()

    def update_level(self):
        new_value = self.read_from_gpio()
        logging.debug('New pulse value: %s', new_value)
        self.value.notify_of_external_update(new_value)

    def cancel_update_level_task(self):
        self.timer.stop()

    # def _decrease_position_index(self):
    #     if (self._position_index==0):
    #         self._position_index = len(FakePositionDevice._values)-1
    #     else:
    #         self._position_index-+1

    # def _increase_position_index(self):
    #     self._position_index = (self._position_index+1)%len(FakePositionDevice._values)

    def getInitialValue(self):
        return 55

        
    # @staticmethod
    def read_from_gpio(self):
        """Mimic an actual sensor updating its reading every couple seconds."""
        # if (use_static):
        #     if (self.device_id in static_values.keys()):
        #         return static_values[self.device_id]
        #     else:
        #         return 1;
        
        # if (random.random()<0.2):
        #     if (random.random()<0.5):
        #         self._decrease_position_index()
        #     else:
        #         self._increase_position_index()
                # self._position_index = (self._position_index+1)%len(FakePositionDevice._values)

        # self.position = FakePositionDevice._values[self._position_index]
        mu = self._value
        sig = 1
        self._value = np.random.normal(mu,sig,1)
        return self._value
        return 4
        # return FakePositionDevice._values[self._position_index]
