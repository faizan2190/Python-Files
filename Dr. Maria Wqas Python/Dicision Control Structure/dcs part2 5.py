# Write a Python program to check if a character entered by the user is an alphabet or not. If the user enters more than
# one character as input, the program prints some appropriate error message and exit.
char=input('Enter an character:')
if len(char)==1:
    if char.isalpha():
        print('The given character is alphabet')
    elif char.isdigit():
        print('The given character is digit')
    elif char=='!' or char=='@' or char=='#' or char=="$" or char=='%' or char=='^' or char=='&' or char=='*':
        print('The given character is special character')
else:
    print('You have entered more then one character')