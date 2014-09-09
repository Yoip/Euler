mat = open('p081_matrix.txt')
mat = mat.read().strip()
mat = mat.replace('\n',',')
mat = mat.split(',')
mat = [int(i) for i in mat]
