import numpy as np
import time

size = 1000

l1 = range(size)
l2 = range(size)

a1 = np.array(size)
a2 = np.array(size)


start = time.time()
result = [ (x+y) for x,y in zip(l1,l2) ]
print((time.time()-start)*1000)

start = time.time()
result = a1+a2
print((time.time()-start*1000))