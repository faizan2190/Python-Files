#PRINT A PREDEFINED MATRIX ON SCREEN:
m=[[1,2,3],[4,5,6],[7,8,9]]
#for i in m:
   # for j in i:
     #   print(j,end='')
    #print()
    #method 2
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j],end='')
    print()