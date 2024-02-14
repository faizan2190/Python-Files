# Write Python programs to display the following patterns. The number of lines should be taken as input from the user.
# *
# **
# ***
# ****
# .
# .
# .
#
# 1
# 22
# 333
# 4444
# .
# .
# .
n=int(input('enter the limit:'))
for i in range(1,n+1):
    print(str(i)*i)