import numpy as np

a = np.array(
    [
        [1,2,3],
        [5,6,7],
        [9,10,11]
    ]
)

print(a)
print(a.shape)

b = a[:2,1:3]
print(b)

c = a[1:3,1:3]
print(c)