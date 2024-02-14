##Write Python programs to display the following patterns. The number of lines should be taken as input from the user.
##a. *
##**
##***
##****
##.
##.
##.
##
##b. 1
##22
##333
##4444
##.
##.
##.
NumOfLines=int(input('ENTER THE NUMBER OF LINES:'))
for i in range(1,NumOfLines+1):
    print(i*'*')
for i in range(1,NumOfLines+1):
    print(i*str(i))
