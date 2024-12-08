class Agente:
    def __init__(self, nombre):
        self.nombre = nombre

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

class Vendedor(Agente):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def vender_terreno(self, costo):
        print(f"Terreno vendido por {costo}.")

class Arquitecto(Agente):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def diseñar_casa(self):
        print("Casa diseñada.")
        return True

class Contratista(Agente):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def construir_casa(self, tiempo, albañiles):
        print(f"Construcción iniciada. Durará {tiempo} días.")
        for albañil in albañiles:
            albañil.trabajar()
        print("Construcción finalizada.")

class Albañil(Agente):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

# Flujo de Trabajo Simulado

# Inicialización de agentes
propietario = Propietario("Juan", 100000)
vendedor = Vendedor("Pedro")
arquitecto = Arquitecto("Ana")
contratista = Contratista("Luis")
albañiles = [Albañil("Carlos"), Albañil("Miguel")]

# Flujo de trabajo
if propietario.comprar_terreno(vendedor, 30000):
    if arquitecto.diseñar_casa():
        if propietario.aprobar_diseno(5000):
            if propietario.contratar_contratista(contratista, 40000):
                contratista.construir_casa(180, albañiles)