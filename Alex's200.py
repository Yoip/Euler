from time import *
from itertools import *
from euler import *
g = time()
squbes = []
for a in sieve(1000):
    for b in sieve(1000):
        if not a==b:
            squbes.append(sqube(a,b))
h=time()
print(len(squbes))
print(h-g)
c=time()
squbestwo = [i for i in squbes if "200" in str(i)]
d=time()
print(len(squbestwo))
print(d-c)
e=time()
aa = 0
squbesthree = []
for i in sorted(squbestwo):
    if isprimeproof(i):
        print(i)
        squbesthree.append(i)
    aa+=1
    print(aa)
print(squbestwo[323])
f=time()
print(len(squbesthree))
print(f-e)


