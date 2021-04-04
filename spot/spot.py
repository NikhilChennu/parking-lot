import abc


class SpotInterface(abc.ABCMeta):

    @abc.abstractmethod
    def getXCord(self) -> int:
        pass

    @abc.abstractmethod
    def getYCord(self) -> int:
        pass

    @abc.abstractmethod
    def getDist(self, otherSpot):
        pass

    @abc.abstractmethod
    def getId(self):
        pass


class Spot(SpotInterface):

    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def getDist(self, other_spot):
        return (self.y_cord - other_spot.y_cord) ** 2 + (self.x_cord - other_spot.x_cord) ** 2

    def getId(self):
        return "x" + str(self.x_cord) + "y" + str(self.y_cord)

    def getXCord(self) -> int:
        return self.x_cord

    def getYCord(self) -> int:
        return self.y_cord
