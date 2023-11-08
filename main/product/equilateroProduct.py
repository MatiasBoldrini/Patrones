from . import TrianguloProductABC

class EquilateroProduct(TrianguloProductABC):

    def getDescripcion(self) -> str:
        return "Soy un triangulo Equilatero"

    def getSuperficie(self, base: float, altura: float) -> float:
        return base * altura

    def dibujate(self) -> None:
        pass