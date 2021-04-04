from abc import ABCMeta,abstractmethod
from datetime import datetime
from typing import Dict


class FareInterface(ABCMeta):

    @abstractmethod
    def caculateFare(self, vehicle_type : str, start_time : datetime, end_time : datetime) -> float:
        pass

    @abstractmethod
    def updateVehicle(self,vehicle_type : str, amount : float) -> None:
        pass
    @abstractmethod
    def removeVehicle(self, vehicle_type : str) -> None:
        pass

class FareManager(FareInterface):

    def __init__(self):
        self.vehicle_fare_map : Dict[str,float]={}

    def updateVehicle(self, vehicle_type : str, amount : float) -> None:
        self.vehicle_fare_map[vehicle_type]=amount

    def removeVehicle(self, vehicle_type : str) -> None:
        del self.vehicle_fare_map[vehicle_type]

    def caculateFare(self, vehicle_type : str, start_time : datetime, end_time : datetime) -> float:
        return min(1,((end_time-start_time).seconds)/60)*self.vehicle_fare_map[vehicle_type]