# Listas paralelas

'''
nombres = ['Juan', 'Maria', 'Lupe', 'Ernesto','Mario']
edades = [21,25,34,20,18]
'''

nombres = [] 
edades = []

for x in range(5):
    nombre = input('Digite el nombre de la persona ')
    nombres.append(nombre)
    edad = int(input('Digite la edad de la persona '))
    edades.append(edad)

print('Nombre de las personas mayores o iguales a 18 años')

for x in range(5):
    if edades[x] >= 18:
        print('nombre ->',nombres[x])
