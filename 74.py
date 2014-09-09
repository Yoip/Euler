from euler import *
import math
l1 = set([1,44,32,13,10])
l89 = set([89,145,42,20,4,16,37,58])
a = 0
for i in range(1,10000000):
    if not i%500000: print(i,a)
    s=i
    h=[]
    while not s==1 or s==89:
        s = sum([int(j)**2 for j in str(s)])
        h.append(s)
        if s in l1:
            l1.update(h)
            break
        if s in l89:
            l89.update(h)
            a+=1
            break
print(a)
