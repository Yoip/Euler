from Euler import *
def sqube(a,b):
  return a**2*b**3
def isPrimeproof(n):
    nums = []
    for i in range(len(str(n))):
        for a in range(10):
            nums.append(int(str(n)[:i]+str(a)+str(n)[i+1:]))
    for b in nums:
        if isPrime(b):
            return False
    return True
  
