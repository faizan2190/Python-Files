##Write code to check if an entered character is an uppercase or a lowercase alphabet.
char=input('ENTER ANY CHARECTER:')
if 'a'<=char<='z':
    print('LOWER CASE')
elif 'A'<=char<='Z':
    print('UPPER CASE')
else:
    print('not a alphabet')
