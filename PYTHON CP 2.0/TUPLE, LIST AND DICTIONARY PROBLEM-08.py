#Write code to add two matrices of similar dimensions, storing the result in a new matrix.
m=[[1,2,3],[4,5,6],[7,8,9]]
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[]
for r in range(len(m)):
    for c in range (len(m[0])):
        m2+=[m[r][c]+m1[r][c]]
print(m2)

