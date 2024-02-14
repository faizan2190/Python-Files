# The cryptography function crypto takes as input a string (i.e., the name of a file in the
# current directory). The function should print the file on the screen with this
# modification: Every occurrence of string 'secret' in the file should be replaced with
# string 'xxxxxx'.
# I will tell you my secret. But first, I have to explain why it is a secret.
# And that is all I will tell you about my secret.
def crypto(filename):
    file=open(filename,'r')
    file=file.read()
    file=file.replace('secret','xxxx')
    return file
new=input('enter the file name with extension:')
x=crypto(new)
print(x)
