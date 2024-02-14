##Write a Python program to check if a character entered by the user is an uppercase alphabet or a lowercase alphabet. If
##the user enters more than one character or any character other than an alphabet as input, the program prints
##appropriate error messages and exit.
char=input('ENTER A CHARECTER:')
if len(char)==1 and ('a'<=char<='z' or 'A'<=char<='Z') :
    if char.isupper():
        print('upper')
    else:
        print('lower')
else:
    print('you entered more than one charecter or not an alphabet')
