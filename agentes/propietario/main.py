# main.py

import json
import ollama
from actions import (buscar_ofertas_terrenos, obtener_tamaño_terreno, obtener_precio_terreno, comprar_terreno,
                     filtrar_ofertas_terrenos)
from prompts import system_prompt

def obtener_respuesta_llm(mensajes):
    respuesta = ollama.chat(model='llama3', messages=mensajes)
    return respuesta['message']['content']

def extraer_json(texto):
    try:
        a = texto.find('ACCIÓN:')
        b = texto.find('PAUSA')
        if a != -1 and b != -1:
            return json.loads(texto[a+8 : b-1])
        else:
            return json.loads(texto)
    except:
        return None

acciones_disponibles = {
    "buscar_ofertas_terrenos": buscar_ofertas_terrenos,
    "obtener_tamaño_terreno": obtener_tamaño_terreno,
    "obtener_precio_terreno": obtener_precio_terreno,
    "comprar_terreno": comprar_terreno,
    "filtrar_ofertas_terrenos": filtrar_ofertas_terrenos
}

def solicitar_criterios_faltantes(criterios_actuales):
    if 'ubicacion' not in criterios_actuales:
        criterios_actuales['ubicacion'] = input('Por favor, especifique la ubicación del terreno:\n')
    if 'tamaño_min' not in criterios_actuales:
        criterios_actuales['tamaño_min'] = float(input('Por favor, especifique el tamaño mínimo del terreno (m2):\n'))
    if 'tamaño_max' not in criterios_actuales:
        criterios_actuales['tamaño_max'] = float(input('Por favor, especifique el tamaño máximo del terreno (m2):\n'))
    if 'precio_max' not in criterios_actuales:
        criterios_actuales['precio_max'] = float(input('Por favor, especifique el precio máximo del terreno:\n'))
    if 'servicios_basicos' not in criterios_actuales:
        servicios_basicos_respuesta = input('¿Requiere que el terreno tenga servicios básicos (agua, electricidad, alcantarillado)? (sí/no):\n')
        criterios_actuales['servicios_basicos'] = servicios_basicos_respuesta.lower() in ['sí', 'si']
    return criterios_actuales

criterios_usuario = input('Describe tus criterios para la compra de terrenos (puedes proporcionar ubicación, rango de tamaño, precio máximo, etc.):\n')

mensajes = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": criterios_usuario},
]

criterios = {}
iteración_actual = 1
máximo_iteraciones = 10
compra_realizada = False
pedir_más_datos = False

while iteración_actual < máximo_iteraciones and not compra_realizada:
    print('TURN ', iteración_actual)
    iteración_actual += 1

    if pedir_más_datos:
        criterios = solicitar_criterios_faltantes(criterios)
        mensajes.append({"role": "user", "content": json.dumps(criterios)})
        pedir_más_datos = False

    respuesta = obtener_respuesta_llm(mensajes)
    print(respuesta)
    print('\n')

    índice_respuesta = respuesta.find("RESPUESTA: ")
    if índice_respuesta != -1:
        print(respuesta[índice_respuesta + 10:])
        break

    json_accion = extraer_json(respuesta)
    print('acción', json_accion)

    if json_accion:
        nombre_funcion = json_accion['nombre_funcion']
        parametros_funcion = json_accion['parametros_funcion']
        if nombre_funcion not in acciones_disponibles:
            raise Exception('Intentó ejecutar una acción no reconocida')
        funcion_accion = acciones_disponibles[nombre_funcion]

        # Convertir valores a números si es necesario
        if parametros_funcion.get('tamaño_min') not in [None, ""]:
            parametros_funcion['tamaño_min'] = float(parametros_funcion['tamaño_min'])
        if parametros_funcion.get('tamaño_max') not in [None, ""]:
            parametros_funcion['tamaño_max'] = float(parametros_funcion['tamaño_max'])
        if parametros_funcion.get('precio_max') not in [None, ""]:
            parametros_funcion['precio_max'] = float(parametros_funcion['precio_max'])

        resultado = funcion_accion(**parametros_funcion)

        if nombre_funcion == "filtrar_ofertas_terrenos" and resultado:
            print("Ofertas filtradas:", resultado)
            if not resultado:
                pedir_más_datos = True
                print("No se encontraron terrenos adecuados. Solicitando más criterios.")
            else:
                for oferta in resultado:
                    if oferta['ubicacion'] == criterios['ubicacion'] and \
                       oferta['tamaño'] >= criterios['tamaño_min'] and \
                       (criterios.get('tamaño_max') is None or oferta['tamaño'] <= criterios['tamaño_max']) and \
                       oferta['precio'] <= criterios['precio_max'] and \
                       (criterios.get('servicios_basicos') is None or oferta['servicios_basicos'] == criterios['servicios_basicos']):
                        respuesta_compra = comprar_terreno(oferta['id_terreno'])
                        mensajes.append({"role": "user", "content": f"RESPUESTA_ACCIÓN: {respuesta_compra}"})
                        print(f"RESPUESTA: El terreno con ID {oferta['id_terreno']} ha sido comprado exitosamente.")
                        compra_realizada = True
                        break
        else:
            mensaje_resultado_accion = f"RESPUESTA_ACCIÓN: {resultado}"
            mensajes.append({"role": "user", "content": mensaje_resultado_accion})

if compra_realizada:
    print("Compra completada. Saliendo del bucle.")
else:
    print("No se encontró ni se compró un terreno adecuado dentro de las iteraciones dadas.")
