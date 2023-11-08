from abc import ABC, abstractmethod

class CommandABC(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass