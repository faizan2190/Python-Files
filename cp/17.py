# # 17. Write code to transpose a matrix, storing the results in a new matric.
# m1=[]
# m=[[1,2,3],[4,5,6],[7,8,9]]
# x=[]
# for i in range(len(m)):
#     for j in range(1):
#         m2=m[i][0]
#     x.append(m2)
# m1.append(x)
# y=[]
# for i in range(len(m)):
#     for j in range(1):
#         m3=m[i][1]
#     y.append(m3)
# m1.append(y)
# z=[]
# for i in range(len(m)):
#     for j in range(1):
#         m4=m[i][2]
#     z.append(m4)
# m1.append(z)
# print(m1)
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         print(m[i][j],end=' ')
#     print()
# print()
# for i in range(len(m1)):
#     for j in range(len(m1[0])):
#         print(m1[i][j],end=' ')
#     print()
d = {3:0, 5:1, 10:1, 8:2, 15:4}

print(d)

for x in d:
    print(x,end=' ')
for x in d.keys():
    print(x,end=' ')
for x in d.values():
    print(x,end=' ')
