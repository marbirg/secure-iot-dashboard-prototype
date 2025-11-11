from webthing import (Action, Event, Property, MultipleThings, Thing, Value,
                      WebThingServer)

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


class MockDimmableLight(Thing):
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

