from . import Color
from . import TV

class Blue(Color):
    def __init__(self) -> None:
        super().__init__()
        self.setDescription("Azul")
        self.es_primario = True

    def colorea(self, tv: TV):
        print(f"Pintando de azul el {tv.getDescription()}")
    
    def setPrimary(self, es_primario: bool) -> None:
        self.es_primario = es_primario

    def isPrimary(self) -> bool:
        return self.es_primario

