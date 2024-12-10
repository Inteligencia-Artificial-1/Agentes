import json
import ollama  # Asegúrate de tener instalada esta biblioteca
from actions import (
    calculate_materials_and_tools,
    receive_payment,
    hire_workers,
    start_construction,
)
from prompts import system_prompt

def get_llm_response(messages):
    """
    Interactúa con el modelo phi3:mini para obtener la respuesta basada en las instrucciones del sistema.
    """
    response = ollama.chat(model='phi3:mini', messages=messages)  # Cambiar a phi3:mini
    return response['message']['content']

def extract_json(text):
    """
    Extrae un objeto JSON válido de la respuesta del modelo, si está presente.
    """
    try:
        a = text.find('ACTION:')
        b = text.find('PAUSE')
        if a != -1 and b != -1:
            return json.loads(text[a + 8 : b - 1])
        else:
            return json.loads(text)
    except Exception:
        return None

available_actions = {
    "calculate_materials_and_tools": calculate_materials_and_tools,
    "receive_payment": receive_payment,
    "hire_workers": hire_workers,
    "start_construction": start_construction,
}

def main():
    print("Bienvenido al sistema de gestión del contratista.")
    user_prompt = input("Describe tu proyecto (ejemplo: Construir una casa de 100m2 en 30 días con 5 albañiles):\n")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    current_iteration = 1
    max_iterations = 10

    while current_iteration <= max_iterations:
        print(f"\nIteración {current_iteration}")
        current_iteration += 1

        # Obtener respuesta del agente
        response = get_llm_response(messages)
        print(f"Respuesta del modelo:\n{response}\n")

        # Verificar si el agente ya tiene una respuesta final
        answer_index = response.find("ANSWER: ")
        if answer_index != -1:
            print(response[answer_index + 8:])
            break

        # Intentar extraer acción del JSON
        json_function = extract_json(response)
        if not json_function:
            print("No se pudo interpretar la acción. Terminando el flujo.")
            break

        # Ejecutar la acción solicitada
        function_name = json_function["function_name"]
        function_params = json_function["function_params"]

        if function_name not in available_actions:
            raise Exception(f"Acción no reconocida: {function_name}")

        action_function = available_actions[function_name]
        result = action_function(**function_params)
        print(f"Resultado de la acción {function_name}: {result}\n")

        # Añadir la respuesta de la acción al historial
        function_result_message = f"ACTION_RESPONSE: {json.dumps(result)}"
        messages.append({"role": "user", "content": function_result_message})

if __name__ == "__main__":
    main()
