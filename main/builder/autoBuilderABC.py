from abc import ABCMeta, abstractmethod
from main.product import AutoProduct

class AutoBuilderABC(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = AutoProduct()

    @property
    def product(self) -> AutoProduct:
        return self._product
    
    @abstractmethod
    def buildMarca(self) -> None:
        pass
    
    @abstractmethod
    def buildModelo(self) -> None:
        pass

    @abstractmethod
    def buildPuertas(self) -> None:
        pass

    @abstractmethod
    def buildMotor(self) -> None:
        pass