# realizar una función que vaide si un numero es positivo y tiene dos digitos
# o negativo y tiene tres digitos
# validar que no sea cero

def testNumero():
    entero = int(input('digite el numero: '))
    if entero == 0:
        return 'El número no puede ser cero'
    elif entero > 0:
        if len(str(entero)) == 2:
            return 'El número es positivo y tiene dos dígitos'
        else:
            return 'El numero es positivo y tiene mas o menos de dos dígitos'
    elif entero < 0:
        if len(str(entero)) - 1 == 3:
            return 'El número es negativo y tiene tres dígitos'
        else:
            return 'El número es negativo y tiene mas o menos de tres dígitos'            

#print(testNumero())


def testNumeroDos():
    numCadena = input('Digite el número: ')

    if numCadena == '0':
        return 'El número no puede ser cero'
    elif numCadena.startswith('-'):
        if len(str(numCadena)) - 1 == 3:
            return 'El número es negativo y tiene tres dígitos'
        else:
            return 'El número es negativo y tiene mas o menos de tres dígitos'            
    else:
        if len(numCadena) == 2:
            return 'El número es positivo y tiene dos dígitos'
        else:
         return 'El numero es positivo y tiene mas o menos de dos dígitos'
         
print(testNumeroDos())