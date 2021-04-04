from abc import ABCMeta, abstractmethod


class VehicleInterface(ABCMeta):

    @abstractmethod
    def slotsNeeded(self) -> int:
        pass

    @abstractmethod
    def getVehicleId(self) -> str :
        pass

    @abstractmethod
    def getVehicleType(self) -> str:
        pass


class Vehicle(VehicleInterface):

    def __init__(self, id):
        super.__init__()
        self.id = id

    def getVehicleId(self) -> str:
        return self.id

    def getVehicleType(self) -> str:
        return self.__class__.__name__


class Car(Vehicle):
    def __init__(self, id):
        Vehicle.__init__(id)
        self.slots = 4

    def slotsNeeded(self) -> int:
        return self.slots

    def getVehicleType(self) -> str:
        pass


class Bike(Vehicle):
    def __init__(self, id):
        Vehicle.__init__(id)
        self.slots = 1

    def slotsNeeded(self) -> int:
        return self.slots

class Truct(Vehicle):
    def __init__(self, id):
        Vehicle.__init__(id)
        self.slots = 16

    def slotsNeeded(self) -> int:
        return self.slots
