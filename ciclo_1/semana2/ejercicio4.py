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


