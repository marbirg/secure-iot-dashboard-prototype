import logging

from webthing import (Action, Event, Property, MultipleThings, Thing, Value,
                      WebThingServer)
from things.mock_PositionDevice import FakePositionDevice
    



class CabCompany:

    def __init__(self, name, nCars=1):
        self.name = name
        self.nCars = nCars
        self.position_devices = []
        self._initPosionDevices()
        pass


    def getPositionDevices(self):
        return self.position_devices

    def _initPosionDevices(self):
        classification = ['private', self.name]
        name_base = self.name + '_car_'
        cars = []
        for i in range(self.nCars):
            name = name_base + str(i)
            cars.append(FakePositionDevice(classification, name))

        self.position_devices = cars
