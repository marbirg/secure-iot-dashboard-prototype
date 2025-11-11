from webthing import (Action, Event, Property, MultipleThings, Thing, Value,
                      WebThingServer)

class FakeMovementSensor(Thing):
    """A sensor that detects movment."""
    _instance_number = 0
    _MIN_VALUE = -20
    _MAX_VALUE = 50

    
    def __init__(self, classification='private'):
        FakeMovementSensor._instance_number+=1
        self._value = False # Initial value
        Thing.__init__(
            self,
            'urn:dev:ops:fake-move-' + str(FakeMovementSensor._instance_number), #id
            'MovementSensor', #title
            ['MovementSensor'], #type
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
                         'title': 'Movement Detected',
                         'type': 'boolean',
                         'description': 'True if movement detected, else False',
                         'readOnly': True,
                     }))

        logging.debug('starting the sensor update looping task')
        self.timer = tornado.ioloop.PeriodicCallback(
            self.update_level,
            3000
        )
        self.timer.start()

    def update_level(self):
        detectedMovement = self.read_from_gpio()
        logging.debug('Movement detected: %s', detectedMovement)
        self.level.notify_of_external_update(detectedMovement)

    def cancel_update_level_task(self):
        self.timer.stop()

    # @staticmethod
    def read_from_gpio(self):
        """Mimic an actual sensor updating its reading every couple seconds."""
        if (False):
            pass
        self._value = self._value + random.random() * (-0.5 + random.random())
        # print("New gpio value:", self._value)
        return self._value
        return abs(self._last_value + random.random() * (-0.5 + random.random()))
