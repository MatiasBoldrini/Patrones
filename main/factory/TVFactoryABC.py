from abc import ABCMeta, abstractmethod
from . import TVFactoryABC
from main.product import Color, TV

class TVFactoryABC(metaclass=ABCMeta):

    @abstractmethod
    def createTV(self) -> Color:
        pass

    @abstractmethod
    def createColor(self, color: Color) -> TV:
        pass

    def assemble(self) -> TV:
        color = self.createColor()
        print(color.getDescription())
        tv = self.createTV(color)
        print(f"Fabricando {tv.getDescription()}")
        return tv
