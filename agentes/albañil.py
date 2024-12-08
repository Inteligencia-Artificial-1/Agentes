from .agentes import Agente

class Albañil(Agente):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def trabajar(self):
        print(f"{self.nombre} está trabajando.")
