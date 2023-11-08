from abc import ABCMeta, abstractmethod
from . import Color
import copy

class TV(metaclass=ABCMeta):
    def __init__(self, brand: str, inches: int, color: Color, price: int) -> None:
        self.brand = brand
        self.inches = inches
        self.color = color
        self.price = price

    def clone(self):
        return copy.copy(self)
