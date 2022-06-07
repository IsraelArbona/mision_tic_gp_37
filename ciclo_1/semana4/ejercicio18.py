# libreria numpy - Tipo de datos
import numpy as np

a = np.array([1,2])
print(type(a))
b = np.array([1.0,2.0])
print(type(b))

c = np.array([1,2], dtype = np.float64)
print(c.dtype)

d = np.array([1.0,2.0], dtype = np.str0)
print(d)