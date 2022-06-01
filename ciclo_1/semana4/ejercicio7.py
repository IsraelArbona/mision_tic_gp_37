from functools import reduce

'''

tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

resultado = list( map( lambda elem: elem if elem % 2 == 0 else 'Impar ' + str(elem), tupla ) )
print(resultado)

'''

# Función reduce

'''
lista = [1,2,3,4,5,6,7,8,9]

acumulador = 0
for elemento in lista:
    acumulador += elemento

print(acumulador)
'''

'''
lista = [1,2,3,4,5,6,7,8,9]
resultado = sum(lista)
print(resultado)
'''

lista = [1,2,3,4,5,6,7,8,9]

def funcion_acumular(acumulador= 0,elemento = 0):
    return acumulador + elemento

# print(funcion_acumular(10,2))

resultado = reduce(funcion_acumular,lista)
print(type(resultado))
print(resultado)

resultado = reduce(lambda acumulador=0, elemento=0: acumulador + elemento, lista)
print(resultado)