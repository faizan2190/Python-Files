# Write code to take integer inputs from user to form a 3x3 matrix.
l=[]
for i in range(3):
    row=input('enter the values of row separated by spaces:')
    row=row.split()

    l.append(row)
print(l)