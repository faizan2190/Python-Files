##Write code to check if an entered character is an alphabet or a digit.
char=input('ENTER A CHARECTER:')
if 'a'<=char<='z' or 'A'<=char<='Z':
    print('alphabet')
elif '0'<=char<='9':
    print('digit')
else:
    print('not a alphabet and digits')
