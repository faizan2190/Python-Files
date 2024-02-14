# Write code to increment a matrix, storing the result in the new matrix.
m=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1=[]
for r in m:
    row=[]
    for j in r:
        row.append(j+1)
    m1.append(row)

print(m)
print(m1)
#or
m=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1=[]
for r in range(len(m)):
    row=[]
    for j in range(len(m[0])):
        row.append(m[r][j]+1)
    m1.append(row)

print(m)
print(m1)

