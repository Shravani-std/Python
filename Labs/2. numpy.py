
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([[6,7,8,9,1], [1,2,3,4,5]])

c = a*2
d = b+2
f = np.dot(a,c)
e = np.random.rand(3,3)

print("First Array: ",a)
print("Second Array: ",b)
print("Third Array: ",c)
print("FOurth Array: ",d)
print("Fifth Array: ",e)
print("Multiplication of first and third array: ",f)