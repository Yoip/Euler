from euler import *
def gen2and5(n, low = 0):
    for i in range(1,n):
        if i > low and not(i % 5) or not(i % 2):
            yield i

def primeproofs(n):
    for i in gen2and5(n, 200):
        if isprimeproof(i):
            yield i
for i in primeproofs(100000):
    if '200' in str(i):print(i)
        
    
