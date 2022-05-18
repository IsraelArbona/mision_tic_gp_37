# Listas en Python

'''
lista = [1,2.5,'DevCode',[5,6],4]

print(lista[0]) # 1
print(lista[1]) # 2.5
print(lista[2]) # DevCode
print(lista[3]) # [5,6]
print(lista[3][0]) # 5
print(lista[3][1]) # 6
print(lista[1:3]) # [2.5, DevCode]
print(lista[1:6]) # toda la lista
print(lista[1:6:2]) # [2.5,[5,6]]
'''

# ejercicio 2

lista = []

# ejercicio 3

'''
nombre = 'Juan'
edad = 27
lista3 = [nombre,edad]
print(lista3)
'''

# ejercicio 4

'''
nombres = ['Ana','Bernardo']
edades = [21,26]
lista4 = [nombres, edades]

print(lista4)

lista4 += ['Luis']
print(lista4)
'''

# ejercicio 7

'''
factura = ['pan', 'huevos', 500,700]
print(factura)

print(len(factura))
print(factura[-1])
'''

# Modificar un valor de la lista

'''
factura[1] = 'carne'
print(factura)
'''

# ejercicio 8
# Método append()
# Este método agrega un elemento al final de la lista.

'''
versiones_plone = [2.5, 3.6, 4, 5]
print(versiones_plone)

versiones_plone.append(6)
print(versiones_plone)
'''

# ejercicio 9
# Método count()
# Este método recibe un elemento como argumento, y cuenta la cantidad que aparece en la lista.

'''
versiones_plone = [2.5, 3.6, 4, 5, 6]
print('6 -> ', versiones_plone.count(6))
print('5 -> ', versiones_plone.count(5))
print('2.5 -> ', versiones_plone.count(2.5))
'''

# Ejercicio 10
# Método extend()
# Este método extiende una lista agregando un itetable al final.

'''
versiones_plone = [2.1, 2.5, 3.6]
print(versiones_plone)
versiones_plone.extend([6.2])
print(versiones_plone)
versiones_plone.extend(range(5,10))
print(versiones_plone)
'''

# ejercicio 11
# Método index()
# Este método recibe un elemnto como argumento 
# y devuelve el índice de su primera aparición en la lista

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
print(versiones_plone.index(4))
print(versiones_plone.index(4,2))
print(versiones_plone.index(4,5))
'''

# el método devuelve una excepción ValueError si el elemento no es encontrado en la lista,
# o en el entorno definido.

'''
print(versiones_plone.index(10))
'''

# Ejercicio 12
# Método insert()
# Este método inserta el elemento x en la lista, en el índice i.

'''
versiones_plone = [2.1, 2.5, 3.6, 4 ,5 ,6]
print(versiones_plone)

versiones_plone.insert(2, 4.5)
print(versiones_plone)
'''

# Ejercicio 13
# Método pop()
# Este método devuelve el último elemento de la lista, y lo borra de la misma

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone.pop())
print(versiones_plone)
'''

# Opcionalmente puede recibir un argumento númerico entero, que funciona como índice
# del elemento( por defecto -1)

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone.pop(2))
print(versiones_plone)
'''

# ejercicio 14
# Método remove()
# Este método recibe como argumento un elemento y borra su primera aparición en la lista.

'''
versiones_plone = [2.1, 2.5, 4,3.6, 4, 5, 6]
print(versiones_plone)

versiones_plone.remove(4)
print(versiones_plone)
'''

# El método devuelve una excepción ValueError si el elemento no se encuentra en la lista.

'''
versiones_plone.remove(11)
'''

# Ejercicio 15
# Método reverse()
# Este método invierte el orden de los elementos de una lista.

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone)

versiones_plone.reverse()
print(versiones_plone)
'''

# Ejercicio 16
# Método sort()
# Este método ordena los elementos de una lista.

versiones_plone = [4, 2.5, 5, 3.7, 1.9, 6]
print(versiones_plone)
versiones_plone.sort()
print(versiones_plone)

# El método sort() admite la opción reverse, por defecto con valor False.
# De tener el valor True, el ordenamiento se hace en sentido inverso.

versiones_plone.sort(reverse = True)
print(versiones_plone)

