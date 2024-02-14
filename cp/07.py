# 6. Input a list of integers from user and store it in a file as:
# i. a list
# ii. as comma separated integer values in a .txt file.
# iii. as comma separated integer values in a .csv file.
value=input('enter the values separated by spaces')
value=value.split()
file=open('check.csv','w')
for i in value:
    file.write(i+'')

