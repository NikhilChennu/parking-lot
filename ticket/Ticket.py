import hashlib
from abc import ABCMeta, abstractmethod
from datetime import datetime

from parkinglot.spot.spot import SpotInterface
from parkinglot.vehicle.vehicle import VehicleInterface


class TicketInterface(ABCMeta):

    @abstractmethod
    def printTicket(self) -> str:
        pass

    @abstractmethod
    def saveTicket(self) -> None:
        pass

    @abstractmethod
    def getVehicleType(self) -> str:
        pass

    @abstractmethod
    def getRegisteredTime(self) -> datetime:
        pass

    @abstractmethod
    def getId(self) -> str:
        pass


class Ticket(TicketInterface):
    def __init__(self, vehicle: VehicleInterface, lot: SpotInterface):
        self.registered_time = datetime.now()
        self.vehicle = vehicle
        self.lot = lot
        self.id = hashlib.md5(str(self.lot.getId() +
                                  self.registered_time.strftime("%y-%m-%d %H:%M:%S.%f") +
                                  self.vehicle.getVehicleType()).encode("utf-8")).hexdigest()[:10]

    def getVehicleType(self) -> str:
        return self.vehicle.getVehicleType()

    def getRegisteredTime(self) -> datetime:
        return self.registered_time

    def printTicket(self) -> str:
        pass

    def saveTicket(self) -> None:
        pass

    def getId(self) -> str:
        return self.id
