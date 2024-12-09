import heapq

# Definición de la prioridad en la cola
class PrioridadCola:
    def __init__(self):
        self.elementos = []

    def empty(self):
        return len(self.elementos) == 0

    def put(self, item, priority):
        heapq.heappush(self.elementos, (priority, item))

    def get(self):
        return heapq.heappop(self.elementos)[1]

# Definición de las propiedades y sus características
class Propiedad:
    def __init__(self, nombre, precio, tamano, ubicacion, servicios):
        self.nombre = nombre
        self.precio = precio
        self.tamano = tamano
        self.ubicacion = ubicacion
        self.servicios = servicios

# Definición del agente Vendedor
class Vendedor:
    def __init__(self, propiedades):
        self.propiedades = propiedades

    def ofrecer(self, preferencias):
        print(f"Buscando propiedades que coincidan con las preferencias: {preferencias}")
        problema = self.crear_problema(preferencias)
        solucion = self.buscar_objetivo(problema)
        return solucion

    def crear_problema(self, preferencias):
        estado_inicial = 'Inicio'
        estados_objetivo = [
            propiedad.nombre for propiedad in self.propiedades if self.cumple_preferencias(propiedad, preferencias)
        ]
        acciones = {'Inicio': {propiedad.nombre: 1 for propiedad in self.propiedades}}
        for propiedad in self.propiedades:
            acciones[propiedad.nombre] = {}
            for otra_propiedad in self.propiedades:
                if propiedad != otra_propiedad:
                    acciones[propiedad.nombre][otra_propiedad.nombre] = 1
        return Problema(estado_inicial, estados_objetivo, acciones)

    def cumple_preferencias(self, propiedad, preferencias):
        for key, value in preferencias.items():
            if getattr(propiedad, key, None) != value:
                return False
        return True

    def buscar_objetivo(self, problema):
        start = problema.estado_inicial
        goal = problema.estados_objetivo
        frontier = PrioridadCola()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current in goal:
                return self.reconstruct_path(came_from, start, current)

            for next in problema.acciones.get(current, {}):
                new_cost = cost_so_far[current] + problema.acciones[current][next]
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put(next, priority)
                    came_from[next] = current

        return None

    def reconstruct_path(self, came_from, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path

# Definición del Problema para el agente vendedor
class Problema:
    def __init__(self, estado_inicial, estados_objetivo, acciones):
        self.estado_inicial = estado_inicial
        self.estados_objetivo = estados_objetivo
        self.acciones = acciones

# Ejemplo de uso
if __name__ == '__main__':
    propiedades = [
        Propiedad('Propiedad 1', 100, 120, 'Centro', ['Piscina']),
        Propiedad('Propiedad 2', 200, 150, 'Norte', ['Gimnasio']),
        Propiedad('Propiedad 3', 300, 200, 'Sur', ['Jardín']),
        Propiedad('Propiedad 4', 100, 100, 'Este', ['Garaje']),
        Propiedad('Propiedad 5', 250, 180, 'Oeste', ['Terraza'])
    ]

    preferencias = {
        'precio': 100,
        'tamano': 100,
        'ubicacion': 'Este'
    }

    vendedor = Vendedor(propiedades)
    solucion = vendedor.ofrecer(preferencias)

    if solucion:
        print("Camino hacia la propiedad encontrada:", solucion)
    else:
        print("No se encontró ninguna propiedad que cumpla con las preferencias.")
