from .agentes import Agente

class Arquitecto(Agente):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def diseñar_casa(self):
        print("Casa diseñada.")
        return True
