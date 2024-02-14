# Write a Python program that accepts a single integer value entered by the user. If the value entered is less than one,
# the program prints nothing. If the user enters a positive integer, n, the program prints an nxn box drawn with *
# characters.
# Test Data:
# Enter value for n: 1
# Expected Output: *
# Enter value for n: 3
# Expected Output: ***
# ***
# ***
n=int(input('enter the number of lines'))
for i in range(n):
    print('*'*3)