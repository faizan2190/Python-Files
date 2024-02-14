#Write code to increment a matrix, storing the result in a SAME matrix.
m=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m)):
    for j in range(len(m[0])):
        m[i][j]=m[i][j]+1

print(m)