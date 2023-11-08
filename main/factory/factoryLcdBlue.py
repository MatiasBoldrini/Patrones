from . import TVFactoryABC
from main.product import Blue, LCD, Color, TV

class FactoryLcdBlue(TVFactoryABC):

    def createColor(self) -> Color:
        return Blue()

    def createTV(self, color: Color) -> TV:
        return LCD( brand="TCL", inches=55, color=color, price=54000, manufacturingCost=32000)
