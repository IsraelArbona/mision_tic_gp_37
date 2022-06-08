# libreria pandas - DataFrame
import pandas as pd

datos = {
    'manzanas': [2,3,4,1,0,4,5,6],
    'naranjas': [5,4,6,7,5,8,9,0]
}

'''
compras = pd.DataFrame(datos)
print(compras)
'''

compras = pd.DataFrame(datos,
                        index=['Juni','Roberto','Lily','David','Marcos','Juliana','Maria','Lucas'])

compras.index.name = 'Clientes'
compras.columns.name = 'Frutas'

print(compras,'\n')
print(compras.axes)
