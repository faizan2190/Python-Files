# 13. Write Python programs to display the following patterns. The number of lines should be taken as input from the user.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# .
# .
# .
#
# b. *
# ***
# *****
# *******
# .
# .
#1
n=int(input('enter the number of lines:'))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=' ')
        num+=1
    print()
#2 
for i in range(1,n+1):
    

