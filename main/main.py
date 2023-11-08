from main.director import AutoDirector
from main.builder import FiatBuilder, FordBuilder, AutoBuilderABC

class Client():

    def __init__(self) -> None:
        self.director = AutoDirector()
        self.autoFord: AutoBuilderABC = FordBuilder()
        self.autoFiat: AutoBuilderABC = FiatBuilder()

    def run(self) -> None:
        for constructor in [self.autoFiat, self.autoFord]:
            self.director.builder = constructor
            self.director.constructAuto()
            auto = self.director.builder
            print(f"Construyendo auto")
            print(f"Marca: {auto.getMarca()}")
            print(f"Modelo: {auto.getModelo()}\n")