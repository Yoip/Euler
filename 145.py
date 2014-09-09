from euler import *
s=0
for i in range(1000):
    #if not i%5000000: print(i, s)
    if str(i)[-1] == '0':
        print('skipped ' + str(i) + " " + str(i+reverse(i)))
        #continue
    print(i,i+reverse(i), s)
    for j in str(i+reverse(i)):
        if not int(j) % 2: break
    else:
        s+=1
