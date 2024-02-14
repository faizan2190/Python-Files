# Write a Python program that takes an integer from the user and determines if it is a prime number. Print appropriate
# messages. Prime numbers are those which have only factors: 1 and the number itself.
num=int(input('enter the integer for prime number: '))
count=0
for i in range(1,num+1):
    if num % i == 0:
        count+=1
if count>2:
    print(f'The given number is not a prime')
else:
    print('The given number is prime')