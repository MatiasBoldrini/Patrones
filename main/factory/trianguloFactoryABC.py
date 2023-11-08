from abc import ABCMeta, abstractmethod
from main.product import TrianguloProductABC

class TrianguloFactoryABC(metaclass = ABCMeta):

    @abstractmethod
    def createTriangulo(self, ladoA: int, ladoB: int, ladoC: int) -> TrianguloProductABC:
        pass
