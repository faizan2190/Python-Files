#INCREAMENT A METRIX AND STORE THEM IN same MATRIX:

m=[[1,2,3],[4,5,6],[7,8,9]]
for r in range(len(m)):
    for c in range(len(m[0])):
        m[r][c]=m[r][c]+1

print(m)
