from . import MotorProduct

class AutoProduct():
    
    def __init__(self) -> None:
        self.marca: str = ""
        self.modelo: str = ""
        self.cantidadPuertas: int = 0
        self.motor: MotorProduct = any

    def getMarca(self) -> str:
        return self.marca
    
    def getModelo(self) -> str:
        return self.modelo
    
    def getCantidadPuertas(self) -> int:
        return self.cantidadPuertas
    
    def getMotor(self) -> MotorProduct:
        return self.motor
    
    def setMarca(self, marca: str) -> None:
        self.marca = marca

    def setModelo(self, modelo: str) -> None:
        self.modelo = modelo

    def setCantidadPuertas(self, cantidadPurtas: int) -> None:
        self.cantidadPuertas = cantidadPurtas

    def setMotor(self, motor: MotorProduct) -> None:
        self.motor = motor
    