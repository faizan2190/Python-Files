# Write code to transpose a matrix, storing the results in a samae matric.
m=[[2, 6, 12], [20, 30, 42], [56, 72, 90]]
m1=[]
for i in range (3):
    for j in range(3):
        m[j][i]=m[i][j]
for row in m:
    print(row)
for row in m:
    print(row)
print(m)
