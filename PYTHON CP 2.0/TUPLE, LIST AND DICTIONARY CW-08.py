#INCREAMENT A METRIX AND STORE THEM IN NEW MATRIX:
m=[[1,2,3],[4,5,6],[7,8,9]]
m1=[]
for r in m:
    row=[]
    for c in r:
        row.append(c+1)
    m1.append(row)
print(m1)
