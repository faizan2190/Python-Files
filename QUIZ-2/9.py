# Write code to multiply two matrices of similar dimensions, storing the result in a new matrix
m=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2=[[2, 3, 4], [5, 6, 7], [8, 9, 10]]
m3=[]
for i in range(len(m)):
    x=[]
    for j in range(len(m[0])):
        x.append(m2[i][j]*m[i][j])
    m3.append(x)
print(m3)