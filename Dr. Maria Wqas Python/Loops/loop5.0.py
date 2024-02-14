# Write a Python program that takes an integer from the user and finds its factorial. Print appropriate messages and the
# result. Also include the special case for printing factorial of 0.

fact=1
n=int(input('Enter the integer for factorial:'))
if n != 0:
    for i in range(1,n+1):
        fact*=i
    print(f'Factorial of the given number is {fact}')
else:
    print(f'Factorial of the given number is 1')