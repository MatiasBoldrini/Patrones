from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass
