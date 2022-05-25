# Conversión de cadenas

# cadena -> listas (String - List)

'''
cadena = 'gurpo 37' # Secuencia inmutable
lista = list(cadena)

print(lista)
'''

# cadena -> tuplas

'''
cadena1 = 'Hola'
cadena2 = 'adios'
numero = 18
tupla1 = tuple(cadena1)
tuplaGeneral = (tupla1,numero,tuple(cadena2))
print(tupla1)
print(tuplaGeneral)
'''

# cadena -> conjuntos (String - Set)

'''
cadena = 'hhola'
print(set(cadena))

cadena2 = '2345948556699'
print(set(cadena2))
'''

# lista -> cadenas (List - String)

'''
lista = ['h','o','l','a',(1,2,3)]

try:
    cadena = ''.join(lista)
    print(cadena)
except:
    print('No se puede concatenar tipos de datos diferentes ha String')

convertirCadena = ''
for elemento in lista:
    convertirCadena = convertirCadena + str(elemento)

print(convertirCadena)
'''

# lista -> tuplas (List - Tuple)

'''
lista = ['h','o','l','a',123]
tupla = tuple(lista)
#print(lista)
print(tupla)
'''

# lista -> cadenas (List - Set)

'''
lista = ['h','o','l','a',1,2,3,]
conjunto = set(lista)
print(conjunto)
'''

# tupla -> cadena (Tuple - Set)

'''
tupla = ('h','o','l','a')
cadena = ''.join(tupla)
print(dir(cadena))
print(cadena)
'''

# tupla -> listas (Tuple - List)

'''
tupla = ('hola',123,'mundo')
lista = list(tupla)
print(lista)
'''

# tupla -> conjuntos (Tuple - Set)

'''
tupla = ('hola',111,'mundo','hola')
conjunto = set(tupla)
conjunto.add(15)
print(conjunto)
'''

# conjunto -> cadenas (Set - String)

'''
conjunto = {'h','o','l','a'}
cadena = ''.join(conjunto)
print(cadena)
'''

# conjunto -> tupla (Set - Tuple)

'''
conjunto = {'h','o','l','a'}
tupla = tuple(conjunto)
print(tupla)
'''

# conjunto -> listas (Set - List)

'''
conjunto = {'h','o','l','a'}
lista = list(conjunto)
print(lista)

lista.sort()
print(lista)
'''

# Conversión de diccionarios

# cadena -> diccionario (Set - Dict)

'''
cadena = 'grupo_37'
diccionario = dict()

for posicion in range(len(cadena)):
    diccionario[posicion]= cadena[posicion]

print(diccionario)

diccionarioZip = dict(zip(range(len(cadena)),cadena))
print(diccionarioZip)
'''

# lista -> diccionario (List - Dict)

'''
lista = ['h','o','l','a']
diccionarioZip = dict(zip(range(len(lista)),lista))
print(diccionarioZip)
'''
# tupla -> diccionario (Tuple - Dict)

'''
tupla = ('h','o','l','a')
diccionarioZip = dict(zip(range(len(tupla)),tupla))
print(diccionarioZip)
'''

# conjunto -> diccionario (Set - Dict)

'''
conjunto = {'h','o','l','a'}
diccionarioZip = dict( zip( range( len( conjunto ) ) ,conjunto ) )
print(diccionarioZip)
'''

# diccionario -> cadena (Dict - String)

'''
dicccionario = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e'
}

cadena = ''.join(dicccionario.values())
print(cadena)
'''

# diccionario -> tupla (Dict - Tuple)

dicccionario = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e'
}

tuplaLlave = tuple(dicccionario.keys())
tuplaValores = tuple(dicccionario.values())
tuplaItems = tuple(dicccionario.items())

print(tuplaLlave)
print(tuplaValores)
print(tuplaItems)
