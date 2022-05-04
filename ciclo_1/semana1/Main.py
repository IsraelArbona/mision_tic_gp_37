# Importar modulos primer metodo
import math
# importar segundo metodo
from math import pi
# importar tercer metodo
from math import *
# importar renombrando el modulo 
import math as m
# importar renombrar las diferentes entidades
from math import pi as PI, sin as seno
# importamos un modulo con sus entidades
from platform import *

#import ejercicio4 as e

from ejercicio4 import cal_Promedio as cpro

'''
print(seno(PI/2))
print(m.sin(m.pi/2))

print(version())
print(platform())
print(processor())
print(system())
'''

print(cpro(3.4, 2, 4.3, 6))
