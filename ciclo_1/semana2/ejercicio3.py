# Forma de clasificar condicionales.

'''
# Dicisión simple
if:

if:
else:

horaDeldia = 11
if horaDeldia >= 12:
    print("PM")
else:
    print("AM")


resultadoDelExamen = 91

if resultadoDelExamen > 60:
    print("Aprobo")
if resultadoDelExamen > 90:
    print("Excelente trabajo")
'''


'''
# Decisiones en secuencia

if:
if:
if:
if:
if:




num = int(input('Digite un número entero '))

if num < 0:
    print('El número digitado es negativo')
if num > 0:
    print('El número digitado es positivo')
if num == 0:
    print('El número es cero')
'''

'''
# Decisiones anidadas

if:
    if:
    else:
else:
    if:
    else:
'''

'''
num = input('Por favor, digite un número entero: ')
num = int(num)

if num < 0:
    num = num * ( -1 )
if ((num >= 1) and (num <= 9)):
    print('El número tiene 1 dígito')
else:
    if (num >= 10) and (num <= 99):
        print('el número tiene 2 dígitos')
    else:
        if (num >= 100) and (num <= 999):
            print('El número tiene 3 dígitos')
        else:
            if num >= 1000 and num <= 9999:
                print('El número tiene 4 dígitos')
            else:
                print('El número tiene mas de 4 dígitos')

# num = int(input('Por favor, digite el número entero: '))

if num < 0:
    num = num * ( -1 )
if (num > 0) and (num < 10):
    print('El número tiene 1 dígito')
elif (num > 9) and (num < 100):
    print('El número tiene 2 dígitos')
elif (num > 99) and (num < 1000):
    print('El número tiene 3 dígitos')
elif (num > 999) and (num < 10000):
    print('El número tiene 4 dígitos')
else:
    print('El número tiene mas de 4 dígitos')
'''


num = int(input('Por favor, ingrese un numero entero: '))

if (num > 0):
    if num > 9 and num < 100:
        print('El numero es positivo y tiene dos digitos')
    else:
        print('El numero es positivo y no tiene dos digitos')
elif num < 0:
    num *= -1
    if num > 99 and num < 1000:
        print('El numero es negativo y tiene 3 digitos')
    else: 
        print('El numero es negativo y no tiene 3 digitos')
else:
    print('El numero es cero') 



