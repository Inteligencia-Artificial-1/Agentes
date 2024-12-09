# actions.py

import requests

def buscar_ofertas_terrenos(ubicacion, criterios):
    return [
        {"id_terreno": 123, "ubicacion": "Pacata Baja", "tamaño": 600, "precio": 95000, "servicios_basicos": True},
        {"id_terreno": 124, "ubicacion": "Pacata Baja", "tamaño": 450, "precio": 85000, "servicios_basicos": False},
        {"id_terreno": 125, "ubicacion": "Pacata Baja", "tamaño": 300, "precio": 50000, "servicios_basicos": True},
        {"id_terreno": 126, "ubicacion": "Pacata Baja", "tamaño": 200, "precio": 30000, "servicios_basicos": True},
        {"id_terreno": 127, "ubicacion": "Pacata Baja", "tamaño": 100, "precio": 25000, "servicios_basicos": False},
        {"id_terreno": 128, "ubicacion": "Pacata Baja", "tamaño": 150, "precio": 20000, "servicios_basicos": True},
        {"id_terreno": 129, "ubicacion": "Pacata Baja", "tamaño": 100, "precio": 30000, "servicios_basicos": True}
    ]

def obtener_tamaño_terreno(id_terreno):
    terrenos = buscar_ofertas_terrenos("Pacata Baja", "")
    for terreno in terrenos:
        if terreno['id_terreno'] == id_terreno:
            return terreno['tamaño']
    return None

def obtener_precio_terreno(id_terreno):
    terrenos = buscar_ofertas_terrenos("Pacata Baja", "")
    for terreno in terrenos:
        if terreno['id_terreno'] == id_terreno:
            return terreno['precio']
    return None

def comprar_terreno(id_terreno):
    return "éxito"

def filtrar_ofertas_terrenos(ofertas_terrenos, ubicacion=None, tamaño_min=None, tamaño_max=None, precio_max=None, servicios_basicos=None):
    ofertas_filtradas = []
    for oferta in ofertas_terrenos:
        if (ubicacion is None or oferta['ubicacion'] == ubicacion) and \
           (tamaño_min is None or oferta['tamaño'] >= tamaño_min) and \
           (tamaño_max is None or oferta['tamaño'] <= tamaño_max) and \
           (precio_max is None or oferta['precio'] <= precio_max) and \
           (servicios_basicos is None or oferta['servicios_basicos'] == servicios_basicos):
            ofertas_filtradas.append(oferta)
    return ofertas_filtradas
