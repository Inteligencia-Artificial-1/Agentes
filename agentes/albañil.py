from threading import Lock
import time

# Diccionario global para controlar el estado de las etapas
estado_etapas = {
    "Preparación_del_terreno": False,
    "Excavación_y_cimentación": False,
    "Construcción_de_muros_de_ladrillo": False,
    "Instalaciones_básicas": False,
    "Enlucido_de_paredes": False,
    "Colocación_de_cerámica_o_baldosas": False,
}

# Bloqueo para sincronización de acceso al estado de etapas
lock = Lock()

# Diccionario de tareas con tiempos de simulación (en segundos)
REGLAS = {
    "Preparación_del_terreno": 5,
    "Excavación_y_cimentación": 10,
    "Construcción_de_muros_de_ladrillo": 8,
    "Instalaciones_básicas": 12,
    "Enlucido_de_paredes": 6,
    "Colocación_de_cerámica_o_baldosas": 7,
}

# Orden de etapas para respetar el flujo de construcción
ORDEN_ETAPAS = list(estado_etapas.keys())


class Albañil:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.habilidades = []

    def entrenar(self, habilidad):
        if habilidad in REGLAS:
            self.habilidades.append(habilidad)
            print(f"{self.nombre} ha sido entrenado en '{habilidad}'.")
        else:
            print(f"Habilidad '{habilidad}' no válida.")

    def trabajar(self, tarea):
        if tarea not in ORDEN_ETAPAS:
            print(f"{self.nombre}: La tarea '{tarea}' no es válida.")
            return

        # Verifica si las etapas anteriores están completas
        index_tarea = ORDEN_ETAPAS.index(tarea)
        for i in range(index_tarea):
            etapa_previa = ORDEN_ETAPAS[i]
            if not estado_etapas[etapa_previa]:
                print(f"{self.nombre} no puede realizar '{tarea}' hasta que se complete '{etapa_previa}'.")
                return

        if tarea in self.habilidades:
            with lock:  # Acceso seguro a `estado_etapas`
                print(f"{self.nombre} ({self.tipo}) está comenzando '{tarea}'. Tiempo estimado: {REGLAS[tarea]} dias.")
                time.sleep(REGLAS[tarea])  # Simula el tiempo de trabajo
                estado_etapas[tarea] = True
                print(f"{self.nombre} ha completado '{tarea}'.")
        else:
            print(f"{self.nombre} no tiene la habilidad para realizar '{tarea}'. Está en espera mientras otros trabajan.")
