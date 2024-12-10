import random

def calculate_materials_and_tools(workers, time_days, house_size_m2):
    """
    Calcula el costo total, la lista de materiales, herramientas y elementos de seguridad
    necesarios para construir la casa.
    """
    # Simulación de cálculos
    base_material_cost = 300 * house_size_m2  # Ejemplo: $300 por m2
    tool_cost_per_worker = 50 * workers       # Ejemplo: $50 por trabajador
    safety_item_cost_per_worker = 20 * workers  # Ejemplo: $20 por trabajador

    total_cost = base_material_cost + tool_cost_per_worker + safety_item_cost_per_worker

    materials_list = ["cement", "bricks", "steel", "sand", "paint"]
    tools_list = ["hammers", "shovels", "ladders", "wheelbarrows"]
    safety_items = ["helmets", "gloves", "safety vests", "goggles"]

    return {
        "total_cost": total_cost,
        "materials_list": materials_list,
        "tools_list": tools_list,
        "safety_items": safety_items,
    }

def receive_payment(amount):
    """
    Simula la recepción del pago por parte del propietario.
    """
    # Para efectos de simulación, asumimos que siempre se recibe el monto
    confirmation = True  # En un caso real, aquí podríamos validar el pago
    return {"confirmation": confirmation}

def hire_workers(workers):
    """
    Simula la contratación de albañiles para el proyecto.
    """
    # Para efectos de simulación, asumimos que siempre se contratan los trabajadores necesarios
    workers_hired = True
    return {"workers_hired": workers_hired}

def start_construction(time_days):
    """
    Simula el proceso de construcción y asegura que se complete en el tiempo estimado.
    """
    # Simulación de éxito del proyecto
    project_completed = random.choice([True, True, False])  # 90% de probabilidad de éxito
    return {"project_completed": project_completed}
