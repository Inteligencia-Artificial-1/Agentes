from main import Agente
class Contratista(Agente):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def construir_casa(self, tiempo, albañiles):
        print(f"Construcción iniciada. Durará {tiempo} días.")
        for albañil in albañiles:
            albañil.trabajar()
        print("Construcción finalizada.")