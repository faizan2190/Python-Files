#take input from user and store them in matrix 3*3
l=[]
for i in range(3):
    row=input('enter row members seperated by space')
    row=row.split()
    row=[int(i) for i in row]
    l.append(row)
print(l)