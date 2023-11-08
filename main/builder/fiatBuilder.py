from main.product import MotorProduct
from . import AutoBuilderABC

class FiatBuilder(AutoBuilderABC):

    def buildMarca(self) -> None:
        self._product.setMarca("Fiat")

    def buildModelo(self) -> None:
        self._product.setModelo("Pulse")

    def buildPuertas(self) -> None:
        self._product.setCantidadPuertas(2)

    def buildMotor(self) -> None:
        motor: MotorProduct = MotorProduct()
        motor.setNumero(123)
        motor.setPotencia("23HP")