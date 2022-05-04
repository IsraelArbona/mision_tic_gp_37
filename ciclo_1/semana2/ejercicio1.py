#Condicionales
'''
var1 = 5
var2 = 5

print(var1 > var2)
print(var1 < var2)
print(var1 != var2)
print(var1 == var2)
print(type(True))
print(type(False))
'''

x = -1

if x > 0:
    print("x es un valor positivo")

# determine si una numero es par o impar

'''
y = 37

if y % 2 == 0:
    print("y es par")
else:
    print("y es impar")  
'''


'''
x = 10
y = 20

if x < y:
    print('"x" es menor que "y"')
elif x > y:
    print('"x" es mayor que "y"')
else:
    print('"x" y "y" son iguales')
'''
'''
letra = 'a'

if letra == 'a':
    print('Mal resultado')
elif letra == 'b':
    print('Buen resultado')
elif letra == 'c':
    print('Cerca, pero no es correcto')
'''

'''
x = 9
y = 32

if x == y:
    print('x e y son iguales')
else:
    if x < y:
        print('x es menor que y')
    else:
        print('x es mayor que y')
'''

# determinar si un numero es de un solo digito

x = 7

if 0 < x:
    if 10 > x:
        print('x es un número positivo de un solo dígito')


if 0 < x and x < 10:
    print('x es un número positivo de un solo dígito')



