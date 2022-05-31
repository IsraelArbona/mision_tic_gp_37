# Envoltura de funciones en python.

'''
def suma(val1 = 0,val2 = 0):
    return val1 + val2

print(suma())

# Asignar una funcion a una variable.
def operacion(funcion, val1 = 0, val2 = 0):
    return funcion(val1,val2)

funcion_suma = suma

resultado = operacion(funcion_suma,10,20)

print(resultado)
'''

# Envoltura de funciones.

'''
def crear_funcion(operador):
    if operador == '+':
        def suma(val1 = 0, val2 = 0):
            return val1 + val2
        return suma
    elif operador == '-':
        def resta(val1 = 0, val2 = 0):
            return val1 - val2
        return resta


def operacion(funcion, val1 = 0, val2 = 0):
    return funcion(val1,val2)

funcion_suma = crear_funcion('+')
resultado = operacion(funcion_suma,15,25)
print(resultado)

funcion_resta = crear_funcion('-')
resultado = operacion(funcion_resta,20,10)
print(resultado)
'''

# Funciones Anónimas. (lambda)

'''
def suma(val1=0, val2=0):
    return val1 + val2

sumar = lambda val1=0,val2=0 : val1 + val2
operacion = lambda operacion,val1=0,val2=0 : operacion(val1,val2)

resultado = operacion(sumar,45,15)
print(resultado)
'''

# Funcion Anonima sin parametros.

'''
sin_parametro = lambda : True
print(sin_parametro() == True)

con_valores = lambda val,val1=0,val2=0 : val + val1 + val2
resultado = con_valores(3,45,19)
print(resultado)
'''

# Funciones Anónimas *args
# *args significa cero o mas argumentos que se almacena en una tupla.

'''
con_asteristo = lambda *args : args[0]
lista = [1,2,3,4,5,6,7,8]

resultado = con_asteristo(*lista)
print(resultado)

resultado = con_asteristo(2)
print(resultado)



def suma(*valores):
    return sum(valores)
resultado = suma(1,2,3,4,5,6,7,8,9)
print(resultado)


suma = lambda *args : args[0] + args[-1]

resultado = suma(10,5)
print(resultado)
'''

# Funcion anonima **kwargs
# **kwargs significa que va a crear un diccionario.

con_doble_asterisco = lambda **args : args['b']

diccionario = {
    'a' : 1,
    'b' : 9
}
resultado = con_doble_asterisco(**diccionario)
print(resultado)


con_doble_asterisco = lambda ** kwargs : sum(kwargs.values())

resultado = con_doble_asterisco(**diccionario)
print(resultado)


lista = [1,2,3,4,5]
dicc = dict({'0' : 1, '1': 2})

con_asteristos = lambda *args, **kwargs : kwargs.get('key', False)

resultado = con_asteristos(*lista,**dicc)
print(resultado)
