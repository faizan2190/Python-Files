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
def cryptography(filename):
    with open(filename,'r') as file:
        content=file.read()
        crypto=content.replace('secret','xxxx')
        # extra kaam
    with open(filename,'w') as file:
        file.write(crypto)
    return crypto
print(cryptography('cryptography.txt'))

