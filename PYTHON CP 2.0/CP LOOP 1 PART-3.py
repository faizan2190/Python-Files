##Write a Python program that takes an integer from the user and prints its times table up to 10.
table=int(input('ENTER THE NUMBER OF TABLE:'))
times=int(input('ENTER THE NUMBER OF TIMES:'))
for i in range(1,times+1):
    print(table,'*',i,'=',table*i)
