from .agentes import Agente

class Vendedor(Agente):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def vender_terreno(self, costo):
        print(f"Terreno vendido por {costo}.")
