from abc import ABCMeta, abstractmethod
from typing import Dict

from parkinglot.id.personal_id import Id
from parkinglot.payment.payment import PaymentInterface
from parkinglot.payment.payment_receit import PaymentNotifier
from parkinglot.resources.logic import LogicInterface
from parkinglot.spot.spot import SpotInterface
from parkinglot.ticket.Ticket import TicketInterface
from parkinglot.ticket.Ticket import Ticket
from parkinglot.vehicle.vehicle import Vehicle
from parkinglot.fare.fare import FareManager

from parkinglot.payment.payment_receit import PrintReceit


from parkinglot.gate.exceptions import EmptySlotsException

from datetime import datetime

class EntryInterface(ABCMeta):
    @abstractmethod
    def Entry(self, id: Id, vehicle: Vehicle) -> TicketInterface:
        pass

    @abstractmethod
    def addlot(self, vehicle_type : str,  spot: SpotInterface) -> bool:
        pass

    @abstractmethod
    def removelot(self, vehicle_type : str, id: str) -> bool:
        pass


class ExitInterface(ABCMeta):
    def Exit(self, ticket: TicketInterface, payment: PaymentInterface) -> PaymentNotifier:
        pass


class CustomerInterface(ABCMeta):
    def feedback(self, message: str, id: Id):
        pass

    def complaint(self, complaint_type: str, payment_receit: PaymentNotifier):
        pass


class GateManager(EntryInterface, ExitInterface, CustomerInterface):
    def __init__(self, fare_manager : FareManager, x_cord: int, y_cord: int):
        self.logic_interface_map : Dict[str,LogicInterface]={}
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.fare_manager=fare_manager

    def registerVehicle(self,vehicle_type, logic_interface_object):
        if vehicle_type not in self.logic_interface_map:
            self.logic_interface_map[vehicle_type]=logic_interface_object

    def removeVehicle(self,vehicle_type):
        del self.logic_interface_map[vehicle_type]

    def Entry(self, id: Id, vehicle: Vehicle) -> TicketInterface:
        vehicle_type=vehicle.__class__.__name__
        if self.logic_interface_map[vehicle_type].isEmpty():
            raise  EmptySlotsException()
        slot=self.logic_interface_map[vehicle_type].getMinDistSlot()
        return Ticket(vehicle,slot)


    def Exit(self, ticket: TicketInterface, payment: PaymentInterface) -> PaymentNotifier:
        end_time=datetime.now()
        fare=self.fare_manager.caculateFare(ticket.getVehicleType(), ticket.getRegisteredTime(), end_time)
        payment_refid = payment.pay(fare)
        return  PrintReceit(payment_refid,ticket.getId(),ticket.getRegisteredTime(),end_time,payment.paymentMode(),fare)

    def __getDist(self, spot: SpotInterface):
        return (self.y_cord - spot.getYCord())**2  +  (self.x_cord-spot.getYCord())

    def addlot(self, vehicle_type : str, spot: SpotInterface) -> bool:
        dist=self.__getDist(spot)
        self.logic_interface_map[vehicle_type].add(dist,spot)
        return True

    def removelot(self, vehicle_type, id: str) -> bool:
        self.logic_interface_map[vehicle_type].remove(id)
        return True

    def feedback(self, message: str, id: Id):
        pass

    def complaint(self, complaint_type: str, payment_receit: PaymentNotifier):
        pass
