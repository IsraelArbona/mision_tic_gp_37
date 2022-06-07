# Libreria pandas
import pandas as pd

ventas = pd.Series([12,43,25], index = ['Ene','Feb','Mar'])

print(ventas)
print(ventas[0])
print(ventas['Ene'])
print(ventas.dtype)

print(ventas.index)
print(ventas.values)

print()
ventas.name = 'Ventas 2022'
ventas.index.name = 'Meses'

print(ventas)

print(ventas.axes)
print(ventas.shape)
