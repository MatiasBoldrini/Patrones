from main.builder import AutoBuilderABC

class AutoDirector():

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> AutoBuilderABC:
        return self._builder.product

    @builder.setter
    def builder(self, builder: AutoBuilderABC) -> None:
        self._builder = builder

    def constructAuto(self) -> None:
        self._builder.buildMarca()
        self._builder.buildModelo()
        self._builder.buildMotor()
        self._builder.buildPuertas()