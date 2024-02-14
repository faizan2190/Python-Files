#Write code to increment a matrix, storing the result in a new matrix.
m=[[1,2,3],[4,5,6],[7,8,9]]
m1=[]
for i in range(len(m)):
    for j in range(len(m[0])):
        m[i][j]=m[i][j]+1
m1+=m
print(m1)