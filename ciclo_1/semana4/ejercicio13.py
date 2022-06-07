import numpy as np

a = np.array(
    [
        [1,2,3],
        [5,6,7],
        [9,10,11]
    ]
)

'''
print(a)
print(a.shape,'\n')

b = a[:2,1:3]
print(b,'\n')

c = a[1:3,1:3]
print(c,'\n')

d = a[1:3,:2]
print(d)
'''
# Invertir los elementos de las filas de izquierda a derecha
d = np.fliplr(a)
print(d)

# Invertir las columna
d = np.flip(a)
print(d)

