import logging

from webthing import (Action, Event, Property, MultipleThings, Thing, Value,
                      WebThingServer)
import tornado.ioloop
import random

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

class FakePositionDevice(Thing):
    """A sensor that detects movment."""
    _instance_number = 0
    _values = [1,2,3,4]
    
    def __init__(self, classification='private', name=None):
        FakePositionDevice._instance_number+=1
        self.device_id = 'urn:dev:ops:fake-position-' + str(FakePositionDevice._instance_number) #id
        self.name = name if name else self.device_id
        print("Create new device:", self.name)
        self._position_index = random.randint(0, len(FakePositionDevice._values)-1) 
        self._position = FakePositionDevice._values[self._position_index] # Initial value
        Thing.__init__(
            self,
            self.device_id,
            name, #title
            ['DiscretePostitionDevice'], #type
            'A device reporting its position', #description
            classification = classification
        )

        self.position = Value(self._position)
        self.add_property(
            Property(self,
                     'position',
                     self.position,
                     metadata={
                         '@type': 'PositionProperty',
                         'title': 'Position',
                         'type': 'int',
                         'description': 'An integer describing position zone',
                         'readOnly': True,
                     }))

        logging.debug('starting the sensor update looping task')
        self.timer = tornado.ioloop.PeriodicCallback(
            self.update_level,
            3000
        )
        self.timer.start()

    def update_level(self):
        new_position = self.read_from_gpio()
        logging.debug('New position: %s', new_position)
        self.position.notify_of_external_update(new_position)

    def cancel_update_level_task(self):
        self.timer.stop()


    def _decrease_position_index(self):
        if (self._position_index==0):
            self._position_index = len(FakePositionDevice._values)-1
        else:
            self._position_index-+1

    def _increase_position_index(self):
        self._position_index = (self._position_index+1)%len(FakePositionDevice._values)
        
    # @staticmethod
    def read_from_gpio(self):
        """Mimic an actual sensor updating its reading every couple seconds."""
        if (use_static):
            if (self.device_id in static_values.keys()):
                return static_values[self.device_id]
            else:
                return 1;
        
        if (random.random()<0.2):
            if (random.random()<0.5):
                self._decrease_position_index()
            else:
                self._increase_position_index()
                # self._position_index = (self._position_index+1)%len(FakePositionDevice._values)

        # self.position = FakePositionDevice._values[self._position_index]
        return FakePositionDevice._values[self._position_index]
