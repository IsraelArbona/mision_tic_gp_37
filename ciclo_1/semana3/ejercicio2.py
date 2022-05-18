# Bucle for
# range(inicio,stop,step)
# range(inicio, fin, contador)

'''
for x in range(0,4):
    print('Estamos en la iteración: ', str(x))
'''

# ejercicio 2

'''
for x in range(0,10,2):
    print('Estamos en la iteración: ', str(x))
'''

# ejercicio 3

'''
for x in range(10,0,-2):
    print('Estamos en la iteración: ' + str(x))
'''

'''
for x in range(10,0,-2):
    if x == 6:
        break
    print('Estamos en la iteración: ' + str(x))
'''

# ejercicio 4
# Método split() convertir a una lista cada palabra de la cadena (String)

# parentesis ()
# corchetes []
# llaves {}

'''
oracion = 'Mary entiende muy bien Python'
frases = oracion.split()

print(type(frases))
print(frases)
print(len(frases))
print("La oración analizada es: ", oracion,".\n")

for palabra in range(len(frases)):
    print('Palabra {0}, en la frase su posición es: {1}'.format(frases[palabra],palabra))
'''

# ejercicio 5
# Bucle 'for' con diccionarios

'''
datosBasicos = {
    'nombre' : 'Leonardo Jose',
    'apellidos': 'Caballero Garcia',
    'cedula': 1100232434,
    'fecha_nacimiento': '03/12/1980',
    'lugar_nacimiento': 'Bucaramanga, Santander',
    'nacionalidad': 'Colombiano',
    'estado_civil': 'Soltero'
}

clave = datosBasicos.keys()
valor = datosBasicos.values()

print(clave,'\n')
print(valor,'\n')

cantidad_datos = datosBasicos.items()

for clave, valor in cantidad_datos:
    print(clave + ": " + str(valor))

# print(type(clave))
clave2 = datosBasicos.keys()

for k in clave2:
    print(k, "= " + str(datosBasicos[k]))
'''

# ejercicio 6

'''
frutas = {
    'Fresa': 'roja',
    'Limon': 'verde',
    'Papaya': 'naranja',
    'Manzana': 'amarilla',
    'Guayaba': 'rosa'
}

for nombre, color in frutas.items():
    print(nombre, "es de color",color)

# for llave in frutas.keys():
for llave in frutas:
    print(llave, 'es de color: ', frutas[llave])

'''

# ejercicio 7
# for else

db_connection = '102.0.0.1','5332','root','nomina'
print(type(db_connection))

for parametro in db_connection:
    print(parametro)
else:
    print('El comando de postgreSQL es: $ psql -h {} -p {} -u {} -d {}'.
    format(db_connection[0], db_connection[1],db_connection[2], db_connection[3]))

