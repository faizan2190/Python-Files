# Write code to print a matrix in matrix form (except the square brackets) on the screen.
lst=[]
for i in range(3):
    row=input('enter the members of rows seperated by space:')
    row=row.split()
    row=[int(i) for i in row]
    lst.append(row)
print(lst)
for r in lst:
    for c in r:
        print(c,end=' ')
    print()
