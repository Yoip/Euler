from itertools import *
from euler import *
for i in count(1):
    if len(str(i)) < len(str(i*6)):
        continue
    for j in range(2,7):
        if not samedigits(i, i*j):
            break
    else:
        print(i)
        break
print('Done')
