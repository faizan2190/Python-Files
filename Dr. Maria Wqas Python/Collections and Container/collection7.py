# Write code to increment a matrix, storing the result in the same matrix.
m1=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        m1[i][j]=m1[i][j]+1
print(m1)