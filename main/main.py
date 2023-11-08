from main.factory import FactoryLcdBlue, FactoryPlasmaYellow

class Cliente():

    def run(self):
        factoryLCD = FactoryLcdBlue()
        tv = factoryLCD.assemble()
        print(f"Costo de produccion: {tv.getManufacturingCost()}")
        print("\n")
        factoryPlasma = FactoryPlasmaYellow()
        tv = factoryPlasma.assemble()
        print(f"Angulo de vision: {tv.getVisionAngle()}")
        print(f"Tiempo de respuesta: {tv.getResponseTime()}")