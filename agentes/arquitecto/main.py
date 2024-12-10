import json
import ollama
from actions import (
    recibir_solicitud,
    diseñar_plan,
    colaborar_aprobación,
    entregar_diseño
)
from prompts import system_prompt

def obtener_respuesta_llm(mensajes):
    respuesta = ollama.chat(model='llama3', messages=mensajes)
    return respuesta['message']['content']

def extraer_json(texto):
    try:
        a = texto.find('ACCIÓN:')
        b = texto.find('PAUSA')
        if a != -1 and b != -1:
            return json.loads(texto[a+8:b-2])
        else:
            return json.loads(texto)
    except:
        return None

def es_pregunta_valida(mensaje):
    temas_validos = ["casa", "construcción de casas"]
    return any(tema in mensaje.lower() for tema in temas_validos)

acciones_disponibles = {
    "recibir_solicitud": recibir_solicitud,
    "diseñar_plan": diseñar_plan,
    "colaborar_aprobación": colaborar_aprobación,
    "entregar_diseño": entregar_diseño
}

mensaje_usuario = input("¿Qué deseas que tenga tu casa?\n")

# Validar si la pregunta es válida
if not es_pregunta_valida(mensaje_usuario):
    print("Por favor, vuelve a intentarlo con una pregunta relacionada con casas o construcción de casas.")
else:
    mensajes = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": mensaje_usuario},
    ]

    iteración_actual = 1
    iteraciones_maximas = 5

    while iteración_actual <= iteraciones_maximas:
        print(f"\nTURNO {iteración_actual}")
        iteración_actual += 1

        respuesta = obtener_respuesta_llm(mensajes)
        print("Respuesta del LLM:", respuesta)

        índice_respuesta = respuesta.find("RESPUESTA:")
        if índice_respuesta != -1:
            print("Respuesta Final:", respuesta[índice_respuesta + 10:])
            break

        funcion_json = extraer_json(respuesta)
        print("Función JSON Extraída:", funcion_json)
        if funcion_json:
            nombre_función = funcion_json.get("nombre_función")
            parámetros_función = funcion_json.get("parámetros_función")
            if nombre_función not in acciones_disponibles:
                raise ValueError(f"Función no reconocida: {nombre_función}")

            función_acción = acciones_disponibles[nombre_función]
            resultado = función_acción(**parámetros_función)
            print(f"Resultado de la Acción: {resultado}")

            mensaje_respuesta_acción = f"RESPUESTA_ACCION: {resultado}"
            mensajes.append({"role": "user", "content": mensaje_respuesta_acción})
        else:
            print("No se encontró una acción válida. Esperando más aclaraciones.")

        mensajes.append({"role": "system", "content": respuesta})

    print("\nFlujo de trabajo completo.")
