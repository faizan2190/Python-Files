# Write code to add two matrices of similar dimensions, storing the result in a new matrix.
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[2,3,4],[5,6,7],[8,9,10]]
m3=[]
for i in range(len(m1)):
    m4=[]
    for j in range(len(m1[0])):
        m4.append(m1[i][j]+m2[i][j])
    m3.append(m4)
print(m3)