# Write code to increment a matrix, storing the result in a samw matrix.
m1=[]
m=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m)):
    m2=[]
    for j in range(len(m[0])):
        m2.append(m[i][j]+1)
    m1.append(m2)
print(m1)