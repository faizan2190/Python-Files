# Write a Python program that takes an integer from the user and prints its times table up to 10.
num=int(input('enter the number for table:'))
for i in range(1,11):
    print(f'{num}*{i}={num*i}')
