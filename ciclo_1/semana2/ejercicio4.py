# Acceder a los carateres de uno en uno en la cadena

#ejercicio 1

fruta = 'fresa'

letra = fruta[1]
print(letra)

fruta = 'banana'
letra = fruta[0]
print(letra)

# Conseguir la longitud de una cadena
# ejercicio 2

fruta = 'banana'
print(len(fruta))
longitud = len(fruta)
print(fruta[longitud -1])

print(fruta[-6])

# Rebanadas de una cadena de text o caracteres.
s = 'Monty_Python'

print(s[0:6])
print(s[6:12])

fruta = 'banana'
print(fruta[:3])
print(fruta[3:])

print(fruta[3:3])
print(fruta[:])


# Inmutabilidad de una cadena - Solo es posible crar una nueva cadena

# ejercicio 7
saludo = "Hola, mundo"
# saludo[0] = "j"

nuevo_saludo = 'j' + saludo[1:]
print(nuevo_saludo)


# Operador in, devuelve respuesta booleana si una cadena se encuentra dentro de otra cadena

# ejercicio 8

var1 = 'a'
var2 = 'banana'
print(var1 in var2)

var1 = 'ola'
var2 = 'banana'
print(var1 in var2)

# comparación de cadenas de caracteres

palabra = 'banana'
if palabra == 'banana':
    print('Esta bien, banana')

# ejercicio 10

palabra2 = 'pera'

if palabra2 < 'banana':
    print('Tu palabra ' + palabra2 + ' , viene antes de banana')
elif palabra2 > 'banana':
    print('Tu palabra ' + palabra2 + ' , viene despues de banana')
else:
    print('la palabras son iguales (banana)')



# Conseguir el tipo de dato de una variable 
# y los métodos asociados a este tipo de variable

# ejercicio 11

cadena = 'Grupo_37'
#print(type(cadena))
#print(dir(cadena))

# Convertir una cadena a mayuscula

palabra = 'fresa'
nueva_palabra = palabra.upper()
print(nueva_palabra)

# Retornar la posición de una subcadena dentro de una cadena

palabra = 'banana'
print(palabra.find('a'))

print(palabra.find('na'))
print(palabra.find('na',3))

# Retirar espacios en blaco de los extremos de una cadena
linea = '       Aquí vamos             '
print(linea.strip())

# conseguir una subcadena dentro de otra cadena al inicio
linea = 'Que Tengas Un Buen Día'
print(linea.startswith('Que'))
print(linea.startswith('q'))

print(linea.lower().startswith('q'))
print(linea.lower())

# Pieza del código que permite cortar 
# el host del correo electronico e imprimirlo luego

# conseguir la @
dato = 'stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
enlaposicion = dato.find('@')
print('\n')
print(enlaposicion) # imprime la posición en entero
espacioenblanco = dato.find(' ',enlaposicion)
print((espacioenblanco))
host = dato[enlaposicion+1:espacioenblanco]
print(host)


# Operador de formato

# %s cadena
# %d números

camellos = 42
print('%d' % camellos)

print('He visto %d camellos' % camellos)

nombre = 'Carlos'
numero = 40
print('%s %d' % (nombre,numero))

saludo = 'Hola'
print('%s, Marcos' % (saludo))


# Omitir caracteres especiales

cadena = r'Hola \n mundo'
print(cadena)

# metodo count

cadena = 'un uno, un dos, un tres'

print(cadena.count('un'))       # hay 4, "un" en la cadena
print(cadena.count('un',10))    # hay 1, "un" a partir de la posición 10
print(cadena.count('un',0,10))  # hay 3, "un" en el rango de 0 a 10

# metodo reemplazar

cadena = 'un uno, un dos, un tres'

print(cadena.replace('un', 'xxx'))
print(cadena.replace('un', 'xxxx',2))

# aplicar format

var1 = 10
var2 = 15
suma = var1 + var2

print("el valor es {}".format(12))
print('el valor es {}'.format(12.4354))

print('los valores son {},{} y {}'.format(1,2,3))

print('los valores son {1},{2} y {0}'.format(1,3,2))

# print('los valores son {var1}, {var2}'.format(var1,var2))


# Multiplicar cadenas

cadena = 'Hola' * 3
cadena2 = 'mundo'
print(cadena + cadena2)

# Añadir

mensaje = 'Hola'
mensaje += ' '
mensaje += 'mundo'

print(mensaje)
