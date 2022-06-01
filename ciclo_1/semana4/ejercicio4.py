# importar pow

from math import pow

# La función pow toma dos argumentos, el número y su potencia. 
print(pow(2,3))

numero   = [2,3,4,5,6,4,7,8,2]
potencia = [4,3,6,5,7,4,3,5]

resultado = list( map(pow,numero,potencia) )
print(resultado)