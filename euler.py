from math import *
from collections import *
from itertools import *
def factor(n):
    factors = []
    root = int(sqrt(n)) + 1
    for i in range(1,root):
        if(n%i==0):
            factors.append(int(i))
            factors.append(int(n/i))
    factors.remove(n)
    return factors
def abundants(n):
    a = []
    for i in range(1,n):
        if(sum(factor(i))>=i):
                a.append(i)
    return a
def deficients(n):
    a = []
    for i in range(1,n):
        if(sum(factor(i))<=i):
                a.append(i)
    return a
def perfects(n):
    a = []
    for i in range(1,n):
        if(sum(factor(i))==i):
                a.append(i)
    return a
def rotated(n):
    l = []
    d = deque(str(n))
    for a in range(0,len(d)):
        d.rotate(1)
        l.append(int(''.join(d)))
    return l
def isprime(n):
    if n <= 1:
        return False
    for a in range(2,int(sqrt(n))+1):
        if(n%a==0):
            return False
    return True
def sieve2(n,m=2):
    l=[]
    for i in range(m,n+1):
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            l.append(i)
    return l

def sieve(limit, low = 0):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            if i>=low: yield i
            for n in range(i*i, limit, i):
                a[n] = False
                
def ispandigital(x,y,z=1):
    if sorted(str(x)) == [str(a) for a in range(z,y+1)]:
        return True
    return False
def istriangular(n):
    for i in count(1):
        t = (i*(i+1))/2
        if t > n:
            return False
        if t == n:
            return True
def ispentagonal(n):
    return (sqrt(1 + 24 * n) + 1.0) / 6.0 == int((sqrt(1 + 24 * n) + 1.0) / 6.0)
def isngonal(x,s):
    return (sqrt((8*s-16)*x+(s-4)**2)+s-4)/(2*s-4) == (sqrt((8*s-16)*x+(s-4)**2)+s-4)/(2*s-4)
def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
def lcm(a,b):
    return abs(a*b)/gcd(a,b)
def factorial(n):
    t=1
    for i in range(2,n):
        t*=i
    return t
def reverse(n):
    return int(str(n)[::-1])
def ispalindrome(n):
    return reverse(n)==n
def digitsum(n):
    return sum([int(i) for i in str(n)])