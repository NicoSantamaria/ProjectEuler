squares = 2

def buildMat(dim):
    pos_mat = [None] * (dim+1)
    for i in range(0, dim+1):
        pos_mat[i] = [None] * (dim+1)
    return(pos_mat)

mat = buildMat(squares)

for x in range(0,squares + 1):
    for y in range(0,squares+1):
        mat[x][y] = [x,y]
print(mat)