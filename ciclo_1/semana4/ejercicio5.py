# calcular los grados celsius a fahrenheit

'''
c = [39.2,36.3,31.9,40.5,25.7]
f = list( map( lambda x: (float(9)/5)*x + 32, c ) )

print('Grados Celsius: ', c)
print('Conversión a grados fahrenheit: ', f)
'''

# calcular los grados fahrenheit a celsius

'''
f = [39.2,36.3,31.9,40.5,25.7]
c = list( map( lambda x: (float(5)/9)*(x-32),f ))

print('Grados fahrenheit: ', f)
print('Conversión a grados celsius: ', c)
'''

# Suma de tres listas


lista1 = [1,2,3]
lista2 = [5,6,7,8]
lista3 = [-2,-4,5,6]

resultado = list( map( lambda a,b,c: a+b+c,lista1,lista2,lista3 ) )
print('el resultado de la suma de las tres lista es: ', resultado)

# Suma de dos listas
resultado2 = list( map( lambda a,b: a+b, lista1,lista2 ))
print(resultado2)

resultado3 = list( map( lambda a,b,c: round(2.3*a + 1.5*b - c,1), lista1,lista2,lista3 ) )
print(resultado3)
