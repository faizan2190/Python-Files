##Write code to check if an entered word is a palindrome or not.
word=input('ENTER A WORD:')
if word==word[::-1]:
    print('PALINDROME')
else:
    print('NOT A PALINDROME')
