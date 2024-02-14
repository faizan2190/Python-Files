# Write code to take integer inputs from user to form a 3x3 matrix.
l=[]
for i in range(3):
    row=input('enter the row members separated by spaces:')
    row=row.split()
    row=[int(i) for i in row]
    l.append(row)

print(l)

