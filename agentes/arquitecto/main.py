import json
import ollama

from actions import (
    recibir_solicitud,
    diseñar_plan,
    colaborar_aprobación,
    entregar_diseño
)
from prompts import system_prompt

# Simula obtener una respuesta de un LLM o sistema similar
def obtener_respuesta_llm(mensajes):
    respuesta = ollama.chat(model='llama3', messages=mensajes)
    return respuesta['message']['content']

# Intenta extraer un objeto JSON válido de la respuesta del LLM
def extraer_json(texto):
    try:
        a = texto.find('ACTION:')
        b = texto.find('PAUSE')
        if a != -1 and b != -1:
            print('Función procesada:', texto[a+8:b-1])
            return json.loads(texto[a+8:b-2])
        else:
            return json.loads(texto)
    except:
        return None

# Un diccionario que mapea nombres de funciones a sus implementaciones
acciones_disponibles = {
    "receive_request": recibir_solicitud,
    "design_plan": diseñar_plan,
    "collaborate_approval": colaborar_aprobación,
    "deliver_design": entregar_diseño
}

# Inicializa la conversación
mensaje_usuario = input("¿Qué deseas que tenga tu casa?\n")
mensajes = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": mensaje_usuario},
]

# Bucle principal para manejar el flujo de trabajo del Agente Arquitecto
iteración_actual = 1
iteraciones_maximas = 5
while iteración_actual <= iteraciones_maximas:
    print(f"\nTURNO {iteración_actual}")
    iteración_actual += 1

    # Obtener la respuesta del LLM
    respuesta = obtener_respuesta_llm(mensajes)
    print("Respuesta del LLM:", respuesta)

    # Comprobar si hay una RESPUESTA en la respuesta para concluir
    índice_respuesta = respuesta.find("ANSWER:")
    if índice_respuesta != -1:
        print("Respuesta Final:", respuesta[índice_respuesta + 8:])
        break

    # Extraer JSON si el LLM sugiere una acción
    funcion_json = extraer_json(respuesta)
    print("Función JSON Extraída:", funcion_json)

    if funcion_json:
        nombre_función = funcion_json["function_name"]
        parámetros_función = funcion_json["function_params"]
        if nombre_función not in acciones_disponibles:
            raise ValueError(f"Función no reconocida: {nombre_función}")

        # Ejecutar la función y obtener el resultado
        función_acción = acciones_disponibles[nombre_función]
        resultado = función_acción(**parámetros_función)
        print(f"Resultado de la Acción: {resultado}")

        # Agregar el resultado nuevamente a la conversación
        mensaje_respuesta_acción = f"ACTION_RESPONSE: {resultado}"
        mensajes.append({"role": "user", "content": mensaje_respuesta_acción})
    else:
        print("No se encontró una acción válida. Esperando más aclaraciones.")

    # Agregar la respuesta del LLM a los mensajes
    mensajes.append({"role": "system", "content": respuesta})

print("\nFlujo de trabajo completo.")
