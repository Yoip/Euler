mat = open('p081_matrix.txt')
mat = mat.read().strip()
mat = mat.replace('\n',',')
mat = mat.split(',')
mat = [int(i) for i in mat]
vals = vals2 = [(i,mat[i]) for i in range(79, 6321, 79)]
print('part1')
while vals[-1][0] >= 0:
    ind = 0
    for (i,j) in vals:
        try:
            #print(i, ind)
            if i < 80:
                vals[ind] = (i - 1, j + mat[i-1])
            elif not i % 80:
                vals[ind] = (i - 80, j + mat[i-80])
            else:
                if mat[i-80] > mat[i-1]:
                    vals[ind] = (i - 1, j + mat[i-1])
                else:
                    vals[ind] = (i - 80, j + mat[i-80])
        except:
            pass
        ind += 1
print('part2')
while vals2[-1][0] <= 6299:
    ind = 0
    for (i,j) in vals2:
        try:
            if i > 6320:
                vals2[ind] = (i + 1, j + mat[i+1])
            elif i % 80 == 79:
                vals2[ind] = (i + 80, j + mat[i+80])
            else:
                if mat[i+80] > mat[i+1]:
                    vals2[ind] = (i + 1, j + mat[i+1])
                else:
                    vals2[ind] = (i + 80, j + mat[i+80])
        except:
            pass
        ind += 1
print('part3')
print(min([sum(i) for i in zip([i[1] for i in vals], [i[1] for i in vals2])]))
