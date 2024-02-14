##Write a Python program to check if a character entered by the user is an alphabet or a digit or a special character. If
##the user enters more than one character as input, the program prints some appropriate error message and exit.
char=input('ENTER ANY CHARECTER:')
if len(char)==1:
    if 'a'<=char<='z' or 'A'<=char<='Z':
        print('ALPHABET')
    elif '0'<=char<='9':
        print('DIGIT')
    else:
        print('SPECIAL CHARECTER')
else:
    print('ERROR..! YOU ENTERED MORE THEN ONE CHARECTER')
    
