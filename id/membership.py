from abc import ABCMeta, abstractmethod
from datetime import date, timedelta

from parkinglot.id.personal_id import Id


class Membership(ABCMeta):

    @abstractmethod
    def getLimit(self):
        pass

    @abstractmethod
    def reduceLimit(self, count):
        pass

    @abstractmethod
    def isValid(self):
        pass


class WeeklyMembership(Membership, Id):
    def __init__(self, name: str, mobile: str, limit: int = int("inf")) -> None:
        Id.__init__(name, mobile)
        self.startDate = date.today()
        self.endDate = self.startDate + timedelta(days=7)
        self.limit = limit

    def getLimit(self) -> int:
        return self.limit

    def reduceLimit(self, count) -> None:
        self.limit -= count

    def isValid(self) -> bool:
        return True if (self.limit > 0 and self.endDate <= date.today()) else False
