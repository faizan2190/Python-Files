# Write code to print a matrix in matrix form (except the square brackets) on the screen.
final_lst=[]
for i in range(3):
    row=input('Enter an integer separated by spaces:')
    row=row.split()
    row=[int(i) for i in row]
    final_lst.append(row)
for row in final_lst:
    for col in row:
        print(col,end=' ')
    print()
# 1print(final_lst)