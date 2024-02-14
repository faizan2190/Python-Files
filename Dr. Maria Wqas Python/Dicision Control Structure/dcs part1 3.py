# Write code to check if an entered character is an alphabet or not.
char=input('enter a character:')
if char.isalpha():
    print('The given character is alphabet')
elif char.isdigit():
    print('The given character is digit')
else:
    print('The given character is alphabet nor digit')