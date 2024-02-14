##Write code to check if an entered number is positive, negative or zero. Print appropriate messages.
num=int(input('ENTER THE NUMBER:'))
if num>0:
    print('positive number')
elif num<0:
    print('negative number')
elif num==0:
    print('number is zero')
else:
    print('not a number')
