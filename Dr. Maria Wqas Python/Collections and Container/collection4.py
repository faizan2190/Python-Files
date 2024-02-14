# Write code to take integer inputs from user to form a 3x3 matrix.
final_lst=[]
for i in range(3):
    row=input('Enter an integer separated by spaces:')
    row=row.split()
    row=[int(i) for i in row]
    final_lst.append(row)
print(final_lst)