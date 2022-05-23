# Lista compuestas

lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

'''
print(lista)
print(lista[0])
print(lista[0][0])
'''

'''
for x in range(len(lista[0])):
    print(lista[0][x])

for x in range(len(lista)):
    for k in range(len(lista[x])):
        print(lista[x][k])
'''

#Ejercicio 2


'''
lista2 = [[1,3,5,7,9],[2,4,6,8,10]]

for x in range(len(lista2)):
    suma = 0
    for k in range(len(lista2[x])):
        suma = suma + lista2[x][k]
    print(suma)
'''

#Ejercicio 3

lista3 = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]

'''
suma3 = 0
for x in range(len(lista3)):
    for k in range(len(lista3[x])):
        suma3 = suma3 + lista3[x][k]

print(suma3)
'''


#Ejercicio 4

padres = list()
hijos = list()

for k in range(3):
    pa = input('Ingrese el nombre del Padre. ')
    ma = input('Ingrese el nombre de la Madre. ')
    padres.append([pa,ma])
    cantidad = int(input('Cantidad de hijos en la familia'))
    hijos.append([])
    for x in range(cantidad):
        hijo = input('Ingrese el nombre del Hijo. ')
        hijos[k].append(hijo)

print(padres)
print(hijos)


print('Lista de padres, madres y hijos')
for x in range(len(padres)):
    print('Padre: ',padres[x][0])
    print('Madre: ', padres[x][1])
    for k in range(len(hijos[x])):
        print('Hijo: ', hijos[x][k])

print('Lista de padre con la cantidad de hijos ')

for x in range(len(padres)):
    print('Padre: ', padres[x][0])
    print('hijos: ', len(hijos[x]))