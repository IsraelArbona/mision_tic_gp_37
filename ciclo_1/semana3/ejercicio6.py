# Creación de conjuntos
# El cunjunto contiene tipo de datos iguales
s = {5,1,2,3,4}

# El conjunto contiene diferentes tipo de datos.
print(type(s))
print(s)

s = {True, 3.14, None, False, "Hola mundo", (3,4)}
print(s)

# Un conjunto no puede incluir objetos mutables como listas 
# y diccionarios e incluso conjuntos.

'''
s = {[3,4]}
print(s)
'''

# tipo de aperación que asigna python es diccionario. cuando utilizamos llaves.
s = {}
print(type(s))

# Crear un conjunto vacio
s = set()

# Podemos obtener un conjunto a partir de cualquier objeto iterable.
s1 = set([1,4,5,2,3,6,6])
s2 = set(range(10))
print(s1)
print(s2)

# Los elementos repetidos se eliminan
s = {1,1,2,2}
print(s)

# Crear conjunto a partir de un String

a = set('Hola grupo 37')
print(a)

# Recorrer un conjunto.
conjunto = {1,3,2,9,3,1}
print(conjunto)

for numero in conjunto:
    print(numero)


# Método de los conjunto.
# add(), agregar un elemento al conjunto

setMutable = set([4,3,11,7,5,2,1,4])
print(setMutable)
setMutable.add(22.5555)
setMutable.add(9)
print(setMutable)

# clear(), remover todo los elementos desde el conjunto

setMutable = set([4,3,11,7,5,2,1,4])
print(setMutable)
setMutable.clear()
print(setMutable)

# copy(), realizar una copia del conjunto.

setMutable = set([4,3,11,7,5,2,1,4])
print(setMutable)
setMutableCopy = setMutable.copy()
print(setMutableCopy)

# difference(), devuelve la diferencia entre dos conjuntos mutable o inmutable

setMutable1 = set([4,3,11,7,5,2,1,4])
setMutable2 = set([11,5,9,2,4,8])

print()
print(setMutable1)
print(setMutable2)
print(setMutable1.difference(setMutable2))
print(setMutable2.difference(setMutable1))

# La diferencia también se puede generar de la siguiente manera

a = {1,2,3,4}
b = {2,3}
c = a -b
print(c)

# dos conjuntos son iguales si tiene los mismos elementos
print({1,2,3} == {1,2,3})

# difference_update(), actuliza el cunjunto

print()
conjunto1 = {'python','Zope','ZODB3','pytz'}
print(conjunto1)
conjunto2 = {'python','plone','diazo'}
print(conjunto2)
conjunto1.difference_update(conjunto2)
print(conjunto1)


# discard(), remover un elemento de un conjunto mutable si esta presente.

print()
conjunto1 = {'python','Zope','ZODB3','pytz'}
print(conjunto1)
conjunto1.discard('Zope')
print(conjunto1)

# intersection(), devuelve la intersección entre los conjuntos mutables.

setMutable1 = set([4,3,11,7,5,2,1,4])
setMutable2 = set([11,5,9,2,4,8])

print()
print(setMutable1)
print(setMutable2)
print(setMutable1.intersection(setMutable2))
print(setMutable2.intersection(setMutable1))

# intersection_update(), modificar el conjunto

con1 = {'python','Zope2','pytz'}
con2 = {'python','Plone','diazo','z3c'}
con3 = {'python','django','django-filter'}

print()
print(con1)
print(con2)
print(con3)

con3.intersection_update(con1,con2)

print(con3)

# isdisjoint(), devuelve el valor verdadero si no hay elementos comunes entre los conjuntos.

setMutable1 = set([4,3,11,7,5,2,1,4])
setMutable2 = set([11,5,9,2,4,8])

print()
print(setMutable1)
print(setMutable2)
print(setMutable1.isdisjoint(setMutable2))

# issubset(), devuelve el valor verdadero si el conjunto mutable es un subconjunto del conjunto

setMutable1 = set([4,3,11,7,5,2,1,4])
setMutable2 = set([11,5,9,2,4,8])
setMutable3 = set([11,5,2,4])

print()
print(setMutable1)
print(setMutable2)
print(setMutable3)

print(setMutable2.issubset(setMutable1))
print(setMutable3.issubset(setMutable1))

# pop(), remueve y devuelve un elemento de conjunto

paquetes = {'python', 'zope', 'plone','django'}

print()
print(paquetes)

print('valor aleatorio devuelto es: ', paquetes.pop())

# remove(), buscar y eliminar un elemento del conjunto.

paquetes = {'python', 'zope', 'plone','django'}

print()
print(paquetes)

print(paquetes.remove('django'))

# union() devuleve un conjunto mutable y conjunto inmutable con todos los elementos.

setMutable1 = set([4,3,11,7,5,2,1,4])
setMutable2 = set([11,5,9,2,4,8])

print()
print(setMutable1)
print(setMutable2)
print(setMutable1.union(setMutable2))

# update(), agrega un elemento desde un conjunto.

version_plone_dev = set([5.1,6])
version_plone = set([2.1,2.5,3.6,4])

print()
print(version_plone_dev)
print(version_plone)
version_plone.update(version_plone_dev)
print(version_plone)



