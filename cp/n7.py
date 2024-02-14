# Write code to increment a matrix, storing the result in the same matrix.
m=[[1,2,3],[4,5,6],[7,8,9]]
m1=[]
for i in range(len(m)):
    m2=[]
    for j in range(len(m[0])):
        x=m[i][j]+1
        m2.append(x)
    m1.append(m2)
print(m1)
print(m)