from Euler import *
def sqube(a,b):
  return a**2*b**3
def isPrime(n):
    if n==0:
        return False
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            return False
    return True
def isPrimeProof(n):
    nums = []
    for i in range(len(str(n))):
        for a in range(10):
            nums.append(int(str(n)[:i]+str(a)+str(n)[i+1:]))
    for b in nums:
        if isPrime(b):
            return False
    return True
  
