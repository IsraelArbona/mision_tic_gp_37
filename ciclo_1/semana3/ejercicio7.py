# Inicialización de tareas -- diccionarios
tareas = {
    '01':{
        'descripcion': 'Ir a mercar',
        'estado': 'pendiente',
        'tiempo': 60
    },
    '02': {
        'descripcion': 'Estudiar',
        'estado': 'pendiente',
        'tiempo': 180 
    },
    '03': {
        'descripcion': 'Hacer ejercicio',
        'estado': 'pendiente',
        'tiempo': 50
    }
}

# Crea una nueva tarea
def create(tareas,identificador,tareaNueva):
    tareas[identificador] = tareaNueva
    return tareas

# Listar las tareas pendientes
def read(tareas):
    for identificador, tarea in tareas.items():
        print(identificador, ' - ', end='')
        for nomAtributo,atributo in tarea.items():
            print(atributo, ' , ', end='')
        print()
    print()

# Validar si existe una tarea.
def validarTarea(identificador,tareas):
    if identificador in tareas:
        return True
    else:
        return False

opcion = 0

while opcion != 5:

    print('\n --- Aplicación del CRUD tareas pendientes --- \n')
    print(' 1: Adicionar Tarea')
    print(' 2: Consultar Tarea')
    print(' 3: Actualizar Tarea')
    print(' 4: Eliminar Tarea')
    print(' 5: Salir')

    opcion = int(input('Ingrese una Opción : '))

    if opcion == 1:
        print()
        print('-> Adicionar Tarea.')
        print()

        identificador = str(input('Ingrese el identificador de la tarea : '))
        descripcion = str(input('Ingrese la descripcion de la tarea : '))
        estado = str(input('Ingrese el estado de la tarea : '))
        tiempo = int(input('Ingrese el tiempo de realización de la tarea : '))

        tareaNueva = {
            'descripcion': descripcion,
            'estado': estado,
            'tiempo': tiempo
        }

        # llamado a la función para agregar una tarea al diccionario principal.
        tareas = create(tareas,identificador,tareaNueva)
    elif opcion == 2:
        print()
        print('-> Consultar Tareas')
        print()

        # llamamos la función para consultar las tareas pendientes.
        read(tareas)
    elif opcion == 3:
        print()
        print('-> Actualizar Tarea')
        print()

        identificador = str(input('Ingrese el identificador de la tarea a modificar : '))

        if validarTarea(identificador,tareas):
            nDescripcion = str(input('Nueva descripción : '))
            if nDescripcion:
                tareas[identificador]['descripcion'] = nDescripcion
            nEstado = str(input('Nuevo estado : '))
            if nEstado:
                tareas[identificador]['estado'] = nEstado
            nTiempo = int(input('Nuevo tiempo : '))
            if nTiempo:
                tareas[identificador]['tiempo'] = nTiempo
        else:
            print('No se ha encontrado la tarea')
    elif opcion == 4:
        print()
        print('-> Eliminar Tarea')
        print()

        identificador = str(input('Ingrese el identificador de la tarea a eliminar : '))

        if validarTarea(identificador, tareas):
            tareas.pop(identificador)
        else:
            print('La tarea pendiente no fue encontrada')