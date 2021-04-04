from abc import ABCMeta, abstractmethod

from parkinglot.spot import SpotInterface


class LogicInterface(ABCMeta):

    @abstractmethod
    def add(self, dist: float, spot: SpotInterface) -> None:
        pass

    @abstractmethod
    def remove(self, spot_id: str) -> None:
        pass

    @abstractmethod
    def isEmpty(self) -> bool:
        pass

    @abstractmethod
    def getMinDistSlot(self) -> SpotInterface:
        pass


class HeapNode():

    def __init__(self, dist: float, spot: SpotInterface) -> None:
        self.dist = dist
        self.spot = spot


class Heap(LogicInterface):


    def __init__(self):
        super().__init__()
        self.heap = []
        self.size = 0
        self.index_map = {}

    def __swap(self, index1, index2):
        self.index_map[self.heap[index1].getId] = index2
        self.index_map[self.heap[index2].getId] = index1
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def __heapifyTopDown(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < self.size and self.heap[index].dist > self.heap[left]:
            smallest = left
        if right < self.size and self.heap[smallest].dist > self.heap[right]:
            smallest = right

        if index != smallest:
            self.__swap(index, smallest)
            self.__heapifyTopDown(smallest)

    def __heapifyBotttoUp(self, index):
        curr = index
        while curr > 0:
            parent = (curr - 1) // 2
            if parent >= 0 and self.heap[parent].dist >= self.heap[curr].dist:
                self.__swap(parent, curr)
                curr = parent
            else:
                break

    def add(self, dist: float, spot: SpotInterface) -> None:
        self.heap.append(HeapNode(dist, spot))
        self.index_map[spot.getId()] = self.size
        self.size += 1
        self.__heapifyBotttoUp(self.size - 1)

    def remove(self, spot: str) -> None:
        index = self.index_map[spot]
        self.heap[index].dist = -1
        self.__heapifyBotttoUp(index)
        self.getMinDistSlot()

    def getMinDistSlot(self) -> SpotInterface:
        id=self.heap[0].getId
        self.__swap(0,self.size-1)
        self.size=self.size-1
        del  self.index_map[id]
        heap_node=self.heap.pop()
        return heap_node.spot

    def isEmpty(self) -> bool:
        return True if self.size==0 else False

