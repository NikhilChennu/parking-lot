from abc import ABCMeta, abstractmethod


class Id(ABCMeta):

    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    def setName(self, name):
        self.name = name

    @abstractmethod
    def getName(self):
        return self.name

    @abstractmethod
    def setMobile(self, mobile):
        self.mobile = mobile

    @abstractmethod
    def getMobile(self):
        return self.mobile


class Personal(Id):
    def __init__(self, name, mobile):
        super(name, mobile)
