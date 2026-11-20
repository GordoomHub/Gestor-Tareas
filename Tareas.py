tareas = []

def agregar_tarea(titulo):
    tareas.append(titulo)

def listar_tareas():
    return tareas

def eliminar_tarea(indice):
    return tareas.pop(indice)