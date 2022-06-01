# Funcion Map
# aplicar funcion sobre cada uno de los elementos.

'''
def cuadrado(elemento = 0):
    return elemento * elemento

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

resultado = list(map(cuadrado,lista))
print(resultado)

resultado2 = list(map(lambda elemento : elemento * elemento,lista))
print(resultado2)
'''

def factorial(numero = 0):
    contar = 2
    resultado = 1
    while contar <= numero:
        resultado *= contar
        contar += 1
    return resultado

print(factorial(4))

lista = [2,3,4,5,6,7,8]

resultado = list( map(factorial,lista) )
print(resultado)