# Write a Python program that requests an integer value from the user. If the value is between 1 and 100 inclusive, print
# "OK"; otherwise, do not print anything.
num=int(input('Enter an integer:'))
if 1<= num <= 100:
    print('OK')
else:
    print('out of range')