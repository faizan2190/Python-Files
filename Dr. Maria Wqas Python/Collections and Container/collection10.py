# Write code to transpose a matrix, storing the results in a new matric.
m=[[1,2,3],[4,5,6],[7,8,9]]
m1=[]
m2=[]
m3=[]
matrix=[]

for i in range(3):
    for j in range(1):
        m1.append(m[i][0])
for i in range(3):
    for j in range(1):
        m2.append(m[i][1])

for i in range(3):
    for j in range(1):
        m3.append(m[i][2])
matrix.append(m1)
matrix.append(m2)
matrix.append(m3)
print(m)


print(matrix)
        