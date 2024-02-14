# Write code to increment a matrix, storing the result in a new matrix.\
m1=[[1,2,3],[4,5,6],[7,8,9]]
new_m=[]
for r in range(len(m1)):
    m2=[]
    for c in range(len(m1[0])):
        m2.append(m1[r][c]+1)
    new_m.append(m2)
print(new_m)
