# Write code to add two matrices of similar dimensions, storing the result in the same matrix.
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[2,3,4],[5,6,7],[8,9,10]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        m1[i][j]=m1[i][j]+m2[i][j]
print(m1)