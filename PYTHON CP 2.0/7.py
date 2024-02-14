# 6. Input a list of integers from user and store it in a file as:
# i. a list
# ii. as comma separated integer values in a .txt file.
# iii. as comma separated integer values in a .csv file.


# store as a list
# list = input('Enter the numbers seprated by space: ')
# l=list.split()
# integer =[]
# for i in l:
#     integer.append(int(i))
# with open('check.txt','w+') as file:
#     file.write(str(integer))
#
# file = open('check.txt')
# print(file.read())

# as comma seprated by integer values in a .txt file

# list = input('Enter the numbers seprated by space: ')
#
# l=list.split()
# integer =[]
# for i in l:
#     integer.append(i)
# with open('check.txt','a') as file:
#     for j in integer:
#         file.write(j+',')

list = input('Enter the numbers seprated by space: ')

l=list.split()
integer =[]
for i in l:
    integer.append(i)

with open('check.csv','a') as file:
    for j in integer:
        file.write(j+',')