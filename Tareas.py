tareas = []

def agregar_tarea(titulo):
    tareas.append(titulo)

def listar_tareas():
    return tareas

def eliminar_tarea(indice):
    return tareas.pop(indice)

def tareas_prioriyarias(prefijo="!"):
    return[t for t in tareas if t.startswith(prefijo)]