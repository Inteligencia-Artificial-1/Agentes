from .agentes import Agente

ACCIONES = {
    "Preparación_del_terreno": {"costo": 100, "descripcion": "Limpieza y nivelación del terreno"},
    "Excavación_y_cimentación": {"costo": 200, "descripcion": "Excavación de zanjas y construcción de cimientos"},
    "Construcción_de_muros_de_ladrillo": {"costo": 150, "descripcion": "Construcción de muros de ladrillo"},
    "Instalaciones_básicas": {"costo": 250, "descripcion": "Instalación de tuberías y cableado eléctrico"},
    "Enlucido_de_paredes": {"costo": 50, "descripcion": "Enlucido de paredes para acabados iniciales"},
    "Colocación_de_cerámica_o_baldosas": {"costo": 100, "descripcion": "Colocación de cerámica o baldosas en pisos y paredes"},
}

ORDEN_ETAPAS = [
    "Preparación_del_terreno",
    "Excavación_y_cimentación",
    "Construcción_de_muros_de_ladrillo",
    "Instalaciones_básicas",
    "Enlucido_de_paredes",
    "Colocación_de_cerámica_o_baldosas"
]

class Albañil(Agente):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = "experimentado" if tipo == "experimentado" else "ayudante"
        self.habilidades = []
        self.etapa_actual = 0  # Índice de la etapa actual en ORDEN_ETAPAS

    def trabajar(self, tarea):
        if tarea not in ORDEN_ETAPAS:
            print(f"La tarea '{tarea}' no forma parte del procedimiento de construcción.")
            return
        if ORDEN_ETAPAS.index(tarea) > self.etapa_actual:
            print(f"No se puede realizar '{tarea}' antes de completar '{ORDEN_ETAPAS[self.etapa_actual]}'.")
            return
        if tarea not in self.habilidades:
            print(f"{self.nombre} no tiene la habilidad para realizar '{tarea}'.")
            return

        accion = ACCIONES[tarea]
        print(f"{self.nombre} ({self.tipo}) está ejecutando '{accion['descripcion']}' con un costo de Bs. {accion['costo']}.")
        self.etapa_actual += 1

    def entrenar(self, habilidad):
        if habilidad in ACCIONES and habilidad not in self.habilidades:
            self.habilidades.append(habilidad)
            print(f"{self.nombre} tiene la habilidad para realizar '{habilidad}'.")
