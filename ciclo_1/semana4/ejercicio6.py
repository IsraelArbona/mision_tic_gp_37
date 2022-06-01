# Funcion filter

'''
def mayor_a_cinco(elemento):
    return elemento >5

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
print('Numero de elemento de la tupla original: ', len(tupla))

resultado = tuple(filter( lambda e: e>5,tupla))
print('numero de elementos de la tupla filtrada',len(resultado))
print(resultado)
'''


pares = list() # []

for i in range(100):
    if i % 2 == 0:
        pares.append(i)

print(pares)

tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

resultado = list( filter( lambda elem: elem % 2 == 0, tupla ) )
print('Números pares : ', resultado)

resultado = list( filter( lambda elem: elem % 2, tupla ) )
print('Números impares : ', resultado)
