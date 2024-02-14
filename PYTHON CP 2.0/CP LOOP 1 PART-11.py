##Write Python programs to display the following patterns. The number of lines should be taken as input from the user.
##
##1
##1 2
##1 2 3
##1 2 3 4
lines=int(input('ENTER THE NUMBER OF LINES:'))
for i in range(1,lines+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
