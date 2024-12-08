from agentes.propietario import Propietario
from agentes.vendedor import Vendedor
from agentes.arquitecto import Arquitecto
from agentes.contratista import Contratista
from agentes.albañil import Albañil

propietario = Propietario("Juan", 100000)
vendedor = Vendedor("Pedro")
arquitecto = Arquitecto("Ana")
contratista = Contratista("Luis")
albañiles = [Albañil("Carlos"), Albañil("Miguel")]

if propietario.comprar_terreno(vendedor, 30000):
    if arquitecto.diseñar_casa():
        if propietario.aprobar_diseno(5000):
            if propietario.contratar_contratista(contratista, 40000):
                contratista.construir_casa(180, albañiles)
