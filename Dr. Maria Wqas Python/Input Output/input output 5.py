# Input a word from user and print if it is a palindrome or not.
word=input('enter a word:')
if word[0:]==word[::-1]:
    print('The given word is palendrome')
else:
    print('The given word is not a palendrome')