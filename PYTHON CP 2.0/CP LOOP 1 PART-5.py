##Write a Python program that takes an integer from the user and prints its factors.
integer=int(input('ENTER THE INTEGER:'))
for i in range(1,integer+1):
    if integer%i==0:
        print(i)
