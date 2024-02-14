# Write code to take integer inputs from user to form a 3x3 matrix.
lst=[]
for i in range(3):
    row=input('enter the members of row separated by space:')
    row =row.split()
    row=[int(i) for i in row]
    lst.append(row)
print(lst)