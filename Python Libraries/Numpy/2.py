import numpy as np

a = np.arange(15).reshape(3,5)

print(a)


for cell in a.flat:
        print(cell)

