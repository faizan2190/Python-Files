##Write a Python program to check if a character entered by the user is an alphabet or not. If the user enters more than
##one character as input, the program prints some appropriate error message and exit.
char=input('ENTER A CHARECTER:')
if len(char)==1:
    if 'a'<=char<='z' or 'A'<=char<='Z':
        print('ALPHABET')
    else:
        print('NOT A ALPHABET')
else:
    print('ERROR..! YOU ENTERED MORE THEN ONE CHARECTER')
    
