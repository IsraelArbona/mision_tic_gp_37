# Declaramos una variable de tipo entero
var_int = 50

# Declaramos una variable de tipo float, double
var_pi = 3.1416

# Declaramos una variable de tipo cadena de texto (string)
var_str = "grupo 37"

# Declaramos una variable de tipo boolean
var_boo = False


# Variable tipo diccionario
var_dict= {
    "nombre":"Juliana",
    "apellido":"Correa",
    "edad":37
}

# Modificar el valor de un campo del diccionario
var_dict["nombre"] = "Maria"
#agregando un nuevo campo al diccionario
var_dict["peso"] = 57.4
# eliminar un campo del diccionario
var_dict.pop("apellido")

'''  comentar un bloque código tres comillas sencillas
print("el nombre de la persona es " + var_dict["nombre"] + " y tiene " + str(var_dict["edad"]))
print("el nombre de la persona es " + var_dict["nombre"] + " y tiene ",var_dict["edad"])
print(f"el nombre de la persona es {var_dict['nombre']} y tiene {var_dict['edad']}")
print("el nombre de la persona es {} y su edad es de {}". format(var_dict["nombre"],var_dict["edad"]))
'''

'''
print(var_int)
print(var_pi)
print(var_str)
print(var_boo)
print(var_dict)
print(var_dict["nombre"])

print(type(var_int))
print(type(var_pi))
print(type(var_str))
print(type(var_boo))
print(type(var_dict))
print(type(var_dict["nombre"]))
'''

x = 1
y = 1.0

z = x + y

print(type(z))



