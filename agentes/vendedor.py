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
class Terreno:
    def __init__(self, nombre, precio, tamano, ubicacion, servicios):
        self.nombre = nombre
        self.precio = precio
        self.tamano = tamano
        self.ubicacion = ubicacion
        self.servicios = servicios

class Vendedor():
    def __init__(self,terrenos):
        self.terrenos = terrenos

    #def ofrecer(self, propiedad , Comprador)
    def ofrecer(self, preferencias):
        print(f"Buscando propiedades que coincidan con las preferencias: {preferencias}")
        problema = self.crear_problema(preferencias)
        solucion = self.buscar_objetivo(problema)
        return solucion
    def crear_problema(self, preferencias):
        estado_inicial = 'Inicio'
        estados_objetivo = [
            terreno.nombre for terreno in self.terrenos if self.cumple_preferencias(terreno, preferencias)
        ]
        acciones = {'Inicio': {terreno.nombre: 1 for terreno in self.terrenos}}
        for terreno in self.terrenos:
            acciones[terreno.nombre] = {}
            for otro_terreno in self.terrenos:
                if terreno != otro_terreno:
                    acciones[terreno.nombre][otro_terreno.nombre] = 1
        return Problema(estado_inicial, estados_objetivo, acciones)

    def cumple_preferencias(self, terreno, preferencias):
        for key, value in preferencias.items():
            if getattr(terreno, key, None) != value:
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
    
    #def vender(self, propiedad, Comprador, precio)
        
    #def comprobar(self, precio, pago)
        
    #def entregar(self, propiedad, Comprador)
        
# Definición del Problema para el agente vendedor
class Problema:
    def __init__(self, estado_inicial, estados_objetivo, acciones):
        self.estado_inicial = estado_inicial
        self.estados_objetivo = estados_objetivo
        self.acciones = acciones
    


if __name__ == '__main__':
    terrenos = [
        Terreno('Terreno 1', 100, 120, 'Centro', ['Luz']),
        Terreno('Terreno 2', 200, 150, 'Norte', ['Alcantarillado']),
        Terreno('Terreno 3', 300, 200, 'Sur', ['Agua']),
        Terreno('Terreno 4', 100, 100, 'Este', ['Luz']),
        Terreno('Terreno 5', 250, 180, 'Oeste', ['Agua'])
    ]
    vendedor = Vendedor(terrenos)

    # Entrada del precio
    while True:
        try:
            print("Presupuesto del terreno que buscas:")
            precio = input()
            precio = int(precio) if precio.strip() != '' else None
            break
        except ValueError:
            print("Por favor, ingresa un número válido para el precio.")

    # Entrada del tamaño
    while True:
        try:
            print("¿Te interesa que tenga algún tamaño?")
            tamanio = input()
            tamanio = int(tamanio) if tamanio.strip() != '' else None
            break
        except ValueError:
            print("Por favor, ingresa un número válido para el tamaño.")

    # Entrada de la ubicación
    print("¿Buscas que esté ubicada en algún lugar?")
    ubicacion = input()
    ubicacion = ubicacion.strip() if ubicacion.strip() != '' else None

    # Construcción de preferencias
    preferencias = {}
    if precio is not None:
        preferencias["precio"] = precio
    if tamanio is not None:
        preferencias["tamano"] = tamanio
    if ubicacion is not None:
        preferencias["ubicacion"] = ubicacion

    # Ofrecer solución
    vendedor = Vendedor(terrenos)
    solucion = vendedor.ofrecer(preferencias)

    if solucion:
        print("Tengo un terreno que te podría interesarte:", solucion)
    else:
        print("No se encontró ningún terreno que cumpla con las preferencias.")

    