from . import TV
from . import Color

class LCD(TV):
    def __init__(self, brand: str, inches: int, color: Color, price: int, manufacturingCost: int) -> None:
        super().__init__(brand, inches, color, price)
        self.manufacturingCost = manufacturingCost
        self.description = "LCD"

    def getManufacturingCost(self) -> int:
        return self.manufacturingCost

    def setManufacturingCost(self, manufacturingCost: int) -> None:
        self.manufacturingCost = manufacturingCost

    def getDescription(self) -> str:
        return self.description
