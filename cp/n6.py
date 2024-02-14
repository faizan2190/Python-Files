# Write code to increment a matrix, storing the result in a new matrix.
m=[[1,2,3],[4,5,6],[7,8,9]]
m1=[]
for row in m:
    m2=[]
    for coloum in row:
        x=coloum+1
        m2.append(x)
    m1.append(m2)
print(m1)

