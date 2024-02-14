# Write Python programs to display the following patterns. The number of lines should be taken as input from the user.
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# .
# .
# .
n=int(input('enter the number of lines:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
