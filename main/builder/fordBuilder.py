from main.product import MotorProduct
from . import AutoBuilderABC

class FordBuilder(AutoBuilderABC):

    def buildMarca(self) -> None:
        self._product.setMarca("Ford")

    def buildModelo(self) -> None:
        self._product.setModelo("Explorer")

    def buildPuertas(self) -> None:
        self._product.setCantidadPuertas(4)

    def buildMotor(self) -> None:
        motor: MotorProduct = MotorProduct()
        motor.setNumero(124)
        motor.setPotencia("25HP")