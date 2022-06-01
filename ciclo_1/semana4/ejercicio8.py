# Función reduce

from functools import reduce

'''
lista = ['Python','Java','Ruby','Elixir']
resultado = reduce(lambda acumulador='',elemento='': acumulador + ' - ' + elemento, lista)
print(resultado)
'''

lista = range(20)

resultado = reduce(lambda x,y: x+y, lista,10)
print(resultado)

