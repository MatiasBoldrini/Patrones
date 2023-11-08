from main.factory import TrianguloFactory, TrianguloFactoryABC
from main.product import TrianguloProductABC

class Cliente():

    def run(self) -> None:
        trianguloFactory: TrianguloFactoryABC = TrianguloFactory()
        print("Bienvenido a la fábrica de triángulos")
        while True:
            data = input("Ingrese la medida de los lados (<ladoA>, <ladoB>, <ladoC>):  ").replace(" ", "").split(",")
            if len(data) != 3:
                print("\n\nFormato Incorrecto")
            else:
                try:
                    for index, element in enumerate(data):
                        data[index] = int(element)
                    break
                except:
                    print("\n\nFormato Incorrecto")
                    continue
        trianguloProduct: TrianguloProductABC = trianguloFactory.createTriangulo(data[0], data[1], data[2])
        print(trianguloProduct.getDescripcion())
