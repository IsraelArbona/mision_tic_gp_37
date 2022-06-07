# libreria numpy - indexación de matrices booleanos
import numpy as np

a = np.array(
    [
        [1,2],
        [3,4],
        [5,6]
    ]
)

print(a, '\n')
bool_idx = (a > 2)

print(bool_idx)

print(a[bool_idx])
print(a[a>2])
