from .agentes import Agente

class Contratista(Agente):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def construir_casa(self, tiempo, albañiles):
        print(f"Construcción iniciada. Durará {tiempo} días.")
        # Lista de tareas a realizar durante la construcción
        tareas = [
            "Contratar_Albañil_Experimentado",
            "Colocación_de_cerámica_o_baldosas",
            "Construcción_de_muros_de_ladrillo",
            "Enlucido_de_paredes"
        ]
        
        for albañil in albañiles:
            print(f"\nAsignando tareas al albañil {albañil.nombre}:")
            for tarea in tareas:
                albañil.trabajar(tarea)
        
        print("\nConstrucción finalizada.")
