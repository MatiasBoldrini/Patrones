from abc import ABCMeta, abstractmethod

class Color(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.description = None

    @abstractmethod
    def colorea(self, tv):
        pass
    
    def getDescription(self) -> str:
        return self.description

    def setDescription(self, description: str) -> None:
        self.description = description