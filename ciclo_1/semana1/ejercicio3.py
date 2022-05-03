# Creación de funciones
def imprime_Cosas():
    print("La clase esta genial")
    print("Python es lo máximo")

# llamar la funcion
#imprime_Cosas()

'''
# Crear función para realizar una suma de dos variables
def operacionSuma():
    a = 4
    b = 2
    suma = a + b
    return "la suma de " + str(a) + " + " + str(b) + " es igual a: " + str(suma)

# Crear función para realizar la suma de dos variable e imprimir
def operacionSumaP():
    a = 5
    b = 7
    suma = a + b
    print("la suma de " + str(a) + " + " + str(b) + " es igual a: " + str(suma))


# llamar la función operacionSuma
resultado = operacionSuma()
print(resultado)

operacionSumaP()

'''

# Creamos una funciona para repetir las funciones anteriormente creadas
def repetir_funciones():
    print("\n")
    imprime_Cosas()
    imprime_Cosas()

#repetir_funciones()

'''
def sumarDosnumeros():
    num1 = float(input("Ingrese el numero 1: "))
    num2 = float(input("Ingrese el numero 2: "))
    print("La suma de",int(num1), "+", int(num2),"es igual a :", int(num1 + num2))

# sumarDosnumeros() 

def raizCuadrada():
    valor = float(input("Por favor, introduzca un numero a calcular su raiz cuadrada: "))
    raiz = valor ** 0.5
    return print("la raiz cuadrada de: ",valor, "es",valor ** 0.5)

# llamar la funcion de raizCuadrada

#raizCuadrada()

# Crear una función con parametros

def suma(a,b):
    return a + b

# print(suma(15,5))

A = 12
B = 28

# print(suma(A,B))
'''

def mi_funcion(nombre, apellido):
    miNombre = nombre + apellido
    return miNombre

# print(mi_funcion("Luis", "Molero"))



# Creamos la función 
def saludar(nombre, mensaje = 'Hola'):
    print(mensaje, nombre)

#llamar la función
#saludar("Pepe Grillo")

def mensaje():
    print("Ingrese por favor un valor")

def sumarDosnumeros():
    mensaje()
    num1 = float(input())
    mensaje()
    num2 = float(input())
    return print("La suma de", num1,"+",num2,"es igual a: ", num1 + num2)

#llamar la función
#sumarDosnumeros()   



# Funciones anidadas

'''
def primeraFuncion(): # función externa
    print("\n \"Hola desde la función externa\" \n")
    def segundaFuncion(): # función interna
        print("\n \"Hola desde la función interna\" \n")
    
    segundaFuncion()

#primeraFuncion()

#mensaje1 = "Hola desde la función externa"
#print(mensaje1)
'''

'''
def primerNumero(x):
    def segundoNumero(y,z):
        return x * y - z
    return segundoNumero

resultado = primerNumero(2)
print(type(resultado))

print(resultado(5,5))
'''

def primeraFuncion():
    x = 2
    def segundaFuncion(a):
        x = 6
        print(a + x)
    print(x)
    # Llamamos la función
    segundaFuncion(3)

# Llamamos la función
primeraFuncion()






