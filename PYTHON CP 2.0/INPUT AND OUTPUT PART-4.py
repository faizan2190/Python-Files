##Input a word from user and print if it is a palindrome or not.
word=input('ENTER A WORD:')
if word==word[::-1]:
    print('palendrome')
else:
    print('not palendrome')
