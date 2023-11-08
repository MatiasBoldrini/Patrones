from abc import ABCMeta, abstractmethod

class TrianguloProductABC(metaclass = ABCMeta):

    def __init__(self, ladoA: int, ladoB: int, ladoC: int) -> None:
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def getLadoA(self) -> int:
        return self.ladoA
    
    def getLadoB(self) -> int:
        return self.ladoB
    
    def getLadoC(self) -> int:
        return self.ladoC
    
    def setLadoA(self, ladoA: int) -> None:
        self.ladoA = ladoA

    def setLadoB(self, ladoB: int) -> None:
        self.ladoB = ladoB

    def setLadoC(self, ladoC: int) -> None:
        self.ladoC = ladoC

    @abstractmethod
    def getDescripcion(self) -> str:
        pass

    @abstractmethod
    def getSuperficie(self, base: float, altura: float) -> float:
        pass
    
    @abstractmethod
    def dibujate(self) -> None:
        pass