# Write a Python program that takes an integer from the user and prints its factors.
num=int(input('enter the number for factors: '))
count=0
for i in range(1,num+1):
    if num%i == 0:
        print(i)