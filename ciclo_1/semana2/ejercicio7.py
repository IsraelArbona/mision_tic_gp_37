# ejercicio tipo Reto

def datosPersonales(Ficha: dict)-> dict:
    uCed = Ficha['Cedula']
    uNom = Ficha['Nombre']
    uApe = Ficha['Apellido']
    uCor = Ficha['Correo']

    # Condición de cedula mayor 100000

    if uCed > 100000:
        condicion = True
    else:
        condicion = False

    dicSalida = dict(Cedula = uCed, Codicion = condicion)

    return dicSalida

Ficha = {
    'Cedula': 11002342342,
    'Nombre': 'Juan',
    'Apellido': 'Lopez',
    'Correo': 'jlopez@gmail.com'
}

print(datosPersonales(Ficha))

'''
    Método clear()
    Este método remueve todos los elementos (items) desde el diccionario
'''

diccionario1 = {
    'cedula': 1100324,
    'nombre': 'Juan',
    'apellido': 'Diaz'
}

print(diccionario1)
diccionario1.clear()
print(diccionario1)

''' 
    Método copy()
    Este método devuelve una copia superficial del tipo diccionario
'''

diccionario1 = {
    'cedula': 1100324,
    'nombre': 'Juan',
    'apellido': 'Lopez'
}

print('diccionario original :', diccionario1)
nuevo_diccionario1 = diccionario1.copy()
print('diccionario copy: ', nuevo_diccionario1)


'''
    fromkeys()
    Este método crea un nuevo diccionario con claves a partir de un tipo de 
    dato secuencial. el valor de values por defecto es el tipo none
'''

lista = ('python', 'zope', 'plone')
version = dict.fromkeys(lista)

print('Nuevo diccionario : %s' % str(version))

version = dict.fromkeys(lista,0.2)
print('Nuevo diccionario: %s' % str(version))


'''
    Método get()
    Devuelve el valor de una clave solicitada. Sino se encuentra nos devuelve none
'''

diccionario2 = {
    'cedula': 1100324,
    'nombre': 'Juan',
    'apellido': 'Lopez'
}

print(diccionario2.get('Cedula'))
print(diccionario2.get('apellido'))
# print(diccionario2['Cedula'])



'''
    Método items()
    Devuelve una lista de pares de diccionario (clave,valor), como una lista de tuplas
'''

diccionario3 = {
    'Cedula': 11002342342,
    'Nombre': 'Juan',
    'Apellido': 'Lopez',
    'Correo': 'jlopez@gmail.com'
}

print(diccionario3.items())

'''
    Método pop()
    Remover especificamente una clave de diccionario y devuelve valor correspondiente,
    Lanza un excepción KeyError si la clave no es encontrada.
'''

diccionario4 = {
    'Cedula': 11002342342,
    'Nombre': 'Juan',
    'Apellido': 'Lopez',
    'Correo': 'jlopez@gmail.com'
}

print('Version Original: ', diccionario4)

nuevo_diccionario4 = diccionario4.pop('Correo')
print('valor eliminado: ', nuevo_diccionario4)
print('Nuevo diccionario:', diccionario4)


'''
    Método update()
    Actualizar un diccionario agregando nuevos pares clave-valor en un segundo diccionario.
    si se llama update sin parametros, el diccionario permanece sin cambio.
'''

diccionario5 = {
    'Cedula': 11002342342,
    'Nombre': 'Juan',
    'Apellido': 'Lopez',
    'Correo': 'jlopez@gmail.com'
}

print('\nDiccionario5 original: ', diccionario5)

nuevoDiccionario = ({'Telefono': 12343233})
print('\nNuevo Diccionario - complemento', nuevoDiccionario)

diccionario5.update(nuevoDiccionario)
print('\nDiccionario actualizado ', diccionario5)

#Ejercicio 6

usuario_1 = {
    'Cedula': 11002342342,
    'Nombre': 'Juan',
    'Apellido': 'Lopez',
    'Correo': 'jlopez@gmail.com'
}

usuario_2 = {
    'Cedula': 1128302339,
    'Nombre': 'Maria',
    'Apellido': 'Rodriguez',
    'Correo': 'mrodriguez@gmail.com'
}

print('\nCliente 1: \n', usuario_1)
print('\nCliente 2: \n', usuario_2)

usuario_1.update(usuario_2)

print('Usuario actualizados: \n', usuario_1)
print('\n')

for k in usuario_1.keys():
    print(f'{k} = {usuario_1[k]}')



# Funciones integradas en los diccionarios.

'''
    len()
    Esta función devuelve un valor entero con el número de 
    claves de un dicciona especifico
'''

diccionario7 = {
    'Cedula': 11002342342,
    'Nombre': 'Juan',
    'Apellido': 'Lopez',
    'Correo': 'jlopez@gmail.com'
}

print(len(diccionario7))

