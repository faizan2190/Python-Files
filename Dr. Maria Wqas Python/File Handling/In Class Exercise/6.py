# Input a list of integers from user and store it in a file as:
# i. a list
# ii. as comma separated integer values in a .txt file.
# iii. as comma separated integer values in a .csv file.
with open('newfile.csv','w') as file:
    val=input('Enter integers separated by spaces:')
    val=val.split()
    for i in val:
        file.write(i+',')