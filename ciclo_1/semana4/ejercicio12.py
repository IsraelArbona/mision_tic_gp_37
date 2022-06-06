# Libreria numpy 
import numpy as np

'''
a = np.array([
    34,
    25,
    7]
)

print(type(a))
print(a.shape)

print(a[0], a[1], a[2])
a[0] = 5

print(a)
'''

'''
b = np.array([
    [1,2,3],
    [4,5,6]]
)

print(b.shape)
print(b[0,0], b[0,1], b[0,2], b[1,0])
'''

'''
e = np.random.random((3,3))
print(e)
print(e.shape)

arreglo = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(arreglo)
print(arreglo.shape)
'''

matriz = np.zeros((4,4))
print(matriz)

b_one = np.ones((2,3))
print(b_one)

c_full = np.full((5,5),8)
print(c_full)

d = np.eye(4)
print(d)
