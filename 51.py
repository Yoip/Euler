from euler import *
from itertools import *
def something():
    a=1
    g=[combinations(range(a), i) for i in range(1,a)]
    for i in sieve(100000):
        #print(i)
        s = list(str(i))
        if len(s)>a:
            a=len(s)
            g=[combinations(range(a), i) for i in range(1,a)]
        for j in g:
            for k in j:
                t=s
                for l in k:
                    t[l] = '*'
                b=0
                for l in range(10):
                    u=t
                    for m in range(len(t)):
                        if t[m] == '*':
                            u[m] = str(l)
                    if isprime(int(''.join(u))):
                        b+=1
                if b==7:
                    print('Answer: ' + str(i))
                    return i
print(something())
                        
                
