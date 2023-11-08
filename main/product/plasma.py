from . import TV
from . import Color

class Plasma(TV):
    def __init__(self, brand: str, inches: int, color: Color, price: int, visionAngle: int, responseTime: int) -> None:
        super().__init__(brand, inches, color, price)
        self.visionAngle = visionAngle
        self.responseTime = responseTime
        self.description = "Plasma... próximamente será un LED"

    def getVisionAngle(self) -> int:
        return self.visionAngle

    def getResponseTime(self) -> int:
        return self.responseTime
    
    def getDescription(self) -> str:
        return self.description
