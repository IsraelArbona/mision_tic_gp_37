# Ciclos while y for

'''
n = 5
while n > 0: # -> condición se cada vez que ingresa al ciclo
    print(n)
    n = n-1 # -> contador desc
print('Despegue!')
'''

# Ejercicio 1
# break -> terminar el ciclo.

'''
while True:
    Numero = int(input('Ingrese el número: '))
    if Numero % 2 == 0:
        print('El número es par')
        break
    else:
        print('El número es impar')
        break
'''

# ejercicio 2

'''
n = int(input('Por favor, ingrese un múmero mayor a cero: '))
while n > 0:
    print(n)
    print('Correcto!')
    break
'''

'''
n = int(input('Ingrese un número positivo: '))
while n > 0:
    print(n)
    n = n - 1
print('Despegue!')
'''

# Ejercicio 4
# Alejarse de terminación
'''
i = 1
while i > 0:
    print(i)
    i += 1
print('Terminar')
'''

# ejercicio 5
# Brincarse la meta

'''
i = 1
while i < 10:
    print(i)
    i +=2
print('Finalizar!')
'''

# ejercicio 6 
# Problemas de indentación

'''
i = 1
while i < 10:
    print(i)
i = i + 1
print('Finalizar')
'''

# ejercicio 7 
# Olvidar el avance

'''
i = 1
while i < 10:
    print(i)
print('Finalizar')
'''

# ejercicio 8

'''
i = 1
while i < 100:
    i = i + 1  # -> importante el avance en el ciclo
    if i == 67:
        break
    print(i)
'''

# ejercicio 9
# continue -> omitir codigo del ciclo

'''
i = 1
while i < 100:
    i += 1
    if i == 67:
        continue
    print(i)
print('Finalizar')
'''

# ejercicio 10
# Mostrar los primeros 5 números impares saltando el cuarto valor (imprimir 5 de ellos)

'''
n = -1
while n != 11:
    n = n +2
    if n == 7:
        continue
    print(n)
print('Finalizar')
'''

'''
numero = 0
while numero < 11:
    numero = numero + 1
    if numero == 7:
        continue
    if numero % 2:
        print(numero)
        
print('Fin')
'''

'''
i = 0
impar = -1
while i <= 5:
    impar += 2
    i += 1
    if i == 4:
        continue
    print(impar)
print('Fin')
'''

# ejercicio 11

'''
promedio, total, contar = 0.0, 0, 0

print('Introduzca la nota de un estudiante ( -1 para salir)')
nota = int(input())

while nota != -1:
    total += nota
    contar += 1
    print('Introduzca la nota de un estudiante ( -1 para salir)')
    nota = int(input())

promedio = total / contar
print('promedio de notas de los estudiantes es: ' + str(promedio))
'''

# ejercicio 12

'''
promedio, total, contar = 0.0, 0, 0
mensaje = 'Introduzca la nota de un estudiante ( -1 para salir)'

nota = int(input(mensaje))
while nota != -1:
    total += nota
    contar += 1
    nota = int(input(mensaje))
else:
    promedio = total / contar
    print('promedio de notas de los estudiantes es: ' + str(promedio))

'''


a, b = 0,1

while b < 100:
    print(b)
    a,b = b, a + b




