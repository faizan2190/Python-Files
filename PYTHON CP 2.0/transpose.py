# Write code to transpose a matrix, storing the results in a new matric.
m2=[]
m1=[]
a=[]
b=[]
m=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(m)):
    m1.append(m[i][0])
m2.append(m1)

for i in range(len(m)):
    a.append(m[i][1])
m2.append(a)

for i in range(len(m)):
    b.append(m[i][2])
m2.append(b)
print(m2)




