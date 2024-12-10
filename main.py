from agentes.propietario import Propietario # type: ignore
from agentes.vendedor import Vendedor # type: ignore
from agentes.arquitecto import Arquitecto # type: ignore
from agentes.contratista import Contratista # type: ignore
from agentes.albañil import Albañil # type: ignore

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
