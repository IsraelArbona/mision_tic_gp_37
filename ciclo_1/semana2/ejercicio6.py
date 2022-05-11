
# mutables se puede modificar

# ejercicio 1

# Diccionario vacio
diccionario = {}

print(diccionario)
print(type(diccionario))

# Ejecicio 2

# Diccionario vacio usando el constructor dict()
diccionario2 = dict()

print(diccionario2)
print(type(diccionario2))

# Si necesitamos almacenar nuevos valores se separan por coma.

diccionario3 = {
#   clave      : valor
    'total'    : 55,
    'descuento': True,
    'subtotal' : 17.233422,
    'cliente'  : 'Juan'
}

print(diccionario3)

# ejercicio 4

diccionario4 = dict({'uno':1, 'dos':2,'tres':3})

print(diccionario4)

# ejercicio 5

diccionario5 = {
    "gato"   : "chat",
    "perro"  : "chien",
    "caballo": "cheval"
}

diccionario6 = {
    'jefe' : '+57 9760766',
    'Secretaria': '+57 232422'
}

print(diccionario5)
print(diccionario6)


# ejercicio 6

usuario = {
    'nombre' : 'Rafael',
    'edad'   : 26,
    'curso'  : 'Curso de Python',
    'skills': {
        'programacion': True,
        'base_de_datos':False
    },
    'no_medallas':10
}

print(usuario)

# Agregar, obtener o modificar algún valor del diccionario.

usuario['nombre'] = 'Martin' 
print(usuario['nombre'])
usuario['activo'] = 1
print(usuario)



# Ejercicio 7

'''
    Podemos obtener todas las llaves (key) de nuestro diccionario
    utilizando el método keys, de igual forma podemos obtener todo
    los valores del diccionario con el método values
'''

diccionario7 = {
    'Eduardo': 1,
    'Juan': 2,
    'Fernando': 3,
    'Rafael': 4
    }

print(diccionario7.keys())
print(diccionario7.values())

diccionario8 = {
    'Nombre'   :'Sixto Manuel',
    'Apellido' :'Garcia Romero',
    'Cedula'   : 70349233,
    'Direccion': "Cll 34 # 30-1",
    'Telefono' : 4304344,
    'Titulo'   : 'Ingeniero',
    'Ciudad'   : 'Cali',
    'Trabajo'  : 'Independiente'
}

print(diccionario8)

print("Cantidad de datos: ", len(diccionario8), "\n")
print(diccionario8, "\n")
print(diccionario8.keys(), "\n")
print(diccionario8.values(), "\n")

print(f'Numero de datos: {len(diccionario8)}')

for llave in diccionario8.keys():
    print(f'{llave} = {diccionario8[llave]}')
print()

# ejercicio 8

datos = dict(
    id = '904343233',
    nombre = 'Mauro',
    apellido = 'Diaz',
    email = 'mdiaz@micorreo.com.co',
    telefono = 34250332,
    github = '@mdiaz',
    intagram = '@mdiazsites',
    direccio = 'cra 43 # 10 32',
    ciudad = 'Armenia',
    departamento = 'Risaralda',
    pais = 'Colombia'
)

print("Cantidad de datos: ", len(datos))
print(datos)
print()
print(datos.keys())
print()
print(datos.values())
print()

diccionario9 = {
    "clave1" : 789,
    "clave2" : True,
    "clave3" : "Eduardo"
}

print(diccionario9)
print(type(diccionario9))
print(diccionario9['clave1'])
print(type(diccionario9['clave1']))
print(diccionario9['clave2'])
print(type(diccionario9['clave2']))
print(diccionario9['clave3'])
print(type(diccionario9['clave3']))

''' 
    Acceder a valor de clave
    Esta operación le permite acceder a un valor especifico del diccionario
    mediante la clave
'''

diccionario = dict(python=3.9, zope=2.13,plone = '+57 54034',django = 2.5)

print(diccionario['python'])

# Encapsulamiento de Dicccionario.

def promedioNotas2(dicNotas: dict):
    sumatoria = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']
    promedio = round(sumatoria/4, 2)
    return promedio

dicNotas = {}
dicNotas['Nota1'] = 4.3
dicNotas['Nota2'] = 3
dicNotas['Nota3'] = 2
dicNotas['Nota4'] = 4.8

print('El promedio es de: ', promedioNotas2(dicNotas))
