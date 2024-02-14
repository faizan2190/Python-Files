# Write code to print a matrix in matrix form (except the square brackets) on the screen.
m=[[1,2,3],[4,5,6],[7,8,9]]
for row in m:
    for coloum in row:
        print(coloum,end=' ')
    print()
