from euler import *
import math
def blue(x):
    return round(math.sqrt(1/2*(x**2-x)+1/2)+1/2, 2)
for i in range(10**12,10**13):
    print(i, blue(i)/i)
    if blue(i)/i == 0.5: break
print(i)
