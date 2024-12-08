
from main import Agente

class Propietario(Agente):
    def __init__(self, nombre, presupuesto):
        super().__init__(nombre)
        self.presupuesto = presupuesto

    def comprar_terreno(self, vendedor, costo):
        if self.presupuesto >= costo:
            self.presupuesto -= costo
            vendedor.vender_terreno(costo)
            print(f"Terreno comprado por {costo}. Presupuesto restante: {self.presupuesto}")
            return True
        print("No hay suficiente presupuesto para comprar el terreno.")
        return False

    def aprobar_diseno(self, costo):
        if self.presupuesto >= costo:
            self.presupuesto -= costo
            print(f"Diseno aprobado por {costo}. Presupuesto restante: {self.presupuesto}")
            return True
        print("No hay suficiente presupuesto para aprobar el diseno.")
        return False

    def contratar_contratista(self, contratista, costo):
        if self.presupuesto >= costo:
            self.presupuesto -= costo
            print(f"Contratista contratado por {costo}. Presupuesto restante: {self.presupuesto}")
            return True
        print("No hay suficiente presupuesto para contratar al contratista.")
        return False