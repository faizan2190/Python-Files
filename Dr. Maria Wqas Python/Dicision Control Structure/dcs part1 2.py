# Write code to check if an entered number is positive, negative or zero. Print appropriate messages.
num=int(input('enter a number:'))
if num<0:
    print('the given number is negative')
elif num==0:
    print('the given number is zero')
else:
    print('the given number is positive')