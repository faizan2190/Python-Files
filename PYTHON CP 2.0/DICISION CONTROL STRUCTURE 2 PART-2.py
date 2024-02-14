##Write a Python program that requests an integer value from the user. If the value is between 1 and 100 inclusive, print
##"OK"; otherwise, print "OUT OF RANGE".
integer=int(input('ENTER AN INTEGER:'))
if 1<=integer<=100:
    print('OK')
else:
    print('OUT OF RANGE')
