# Write code to print a matrix in matrix form (except the square brackets) on the screen.
l=[]
for i in range(3):
    row=input('enter the values of row separated by spaces:')
    row=row.split()
    row=[int(i) for i in row]
    l.append(row)
for i in range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j],end=' ')
    print()