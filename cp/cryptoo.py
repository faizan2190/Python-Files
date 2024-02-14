# The cryptography function crypto takes as input a string (i.e., the name of a file in the current directory). The
# function should print the file on the screen with this modification: Every occurrence of string 'secret' in the file should
# be replaced with string 'xxxxxx'.
# Test Data:
# File name:
# crypto.txt
# File contents:
# I will tell you my secret. But first, I have to explain why it is a secret.
# And that is all I will tell you about my secret.
# >> crypto('crypto.txt')
# I will tell you my xxxxxx. But first, I have to explain why it is a xxxxxx.
# And that is all I will tell you about my xxxxxx.
def cryptoo(filename):
    file=open(filename,'r')
    file=file.read()
    file=file.replace('secret','xxxxx')
    return file
filename=input('enter the name of file with extension:')
x=cryptoo(filename)
print(x)