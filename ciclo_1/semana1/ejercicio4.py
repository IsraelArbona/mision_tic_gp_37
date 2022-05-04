# Crear una función
def nombre_genero(letraGenero):
    pass # no se realiza nada en la función
    # return letraGenero

# print(nombre_genero("M"))

# variables notas
nota1 = 3.4
nota2 = 4
nota3 = 2.7
nota4 = 4.6

promedio = (nota1 + nota2 + nota3 + nota4)/4
# print(promedio)

# Crear una función para obtener el promedio de cuatro notas 
# y que su resultado sea un numero entero

def cal_Promedio(n1,n2,n3,n4):
    result = ((n1 + n2 + n3 + n4)/4)
    result = round(result,1)
    # return "El promedio de las notas es " + str(result)
    return result


miResultado = cal_Promedio(nota1, nota2, nota3, nota4)
print("El promedio de las notas es: " + str(miResultado))

'''
# Variables de entrada
nt1 = float(input("Ingrese la nota 1:"))
nt2 = float(input("Ingrese la nota 2:"))
nt3 = float(input("Ingrese la nota 3:"))
nt4 = float(input("Ingrese la nota 4:"))

#Crear la función
def cal_Promedio2(n1,n2,n3,n4):
    return round(((n1+n2+n3+n4)/4),1)

miResultado2 = cal_Promedio2(nt1,nt2, nt3, nt4)
print("El promedio de las notas es: " + str(miResultado2))
'''
