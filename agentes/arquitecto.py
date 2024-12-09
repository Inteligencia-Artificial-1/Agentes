from .agentes import Agente

class Arquitecto(Agente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.estado = "inicial"  # Estados posibles: inicial, borrador, finalizado, aprobado
        self.tiempo_restante = 0  # Días disponibles para la tarea actual
        self.presupuesto = 0      # Presupuesto disponible para las tareas

    def tener_tiempo(self, dias):
        """Configura el tiempo disponible para realizar tareas."""
        self.tiempo_restante = dias
        print(f"{self.nombre}: Tiempo disponible configurado a {dias} días.")

    def diseñar_casa(self, costo=10000, tiempo=30):
        """Diseña la casa considerando el costo y tiempo asignados."""
        if self.tiempo_restante < tiempo:
            print(f"{self.nombre}: No hay suficiente tiempo para diseñar la casa. Tiempo requerido: {tiempo} días.")
            return False
        
        self.tiempo_restante -= tiempo
        self.estado = "borrador"
        print(f"{self.nombre}: Casa diseñada en estado '{self.estado}'. Tiempo restante: {self.tiempo_restante} días.")
        return True

    def colaborar_aprobación(self, costo=5000, tiempo=90):
        """Colabora en la aprobación del diseño."""
        if self.tiempo_restante < tiempo:
            print(f"{self.nombre}: No hay suficiente tiempo para colaborar en la aprobación. Tiempo requerido: {tiempo} días.")
            return False

        self.tiempo_restante -= tiempo
        self.estado = "aprobado"
        print(f"{self.nombre}: Diseño aprobado en estado '{self.estado}'. Tiempo restante: {self.tiempo_restante} días.")
        return True

    def entregar_diseño_aprobado(self, tiempo=21):
        """Entrega el diseño aprobado."""
        if self.tiempo_restante < tiempo:
            print(f"{self.nombre}: No hay suficiente tiempo para entregar el diseño aprobado. Tiempo requerido: {tiempo} días.")
            return False

        self.tiempo_restante -= tiempo
        print(f"{self.nombre}: Diseño aprobado entregado en {tiempo} días. Tiempo restante: {self.tiempo_restante} días.")
        return True

# Ejemplo de integración en el main (simulación)
if __name__ == "__main__":
    arquitecto = Arquitecto("Ana")
    arquitecto.tener_tiempo(150)

    if arquitecto.diseñar_casa():
        if arquitecto.colaborar_aprobación():
            arquitecto.entregar_diseño_aprobado()
