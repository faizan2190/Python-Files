##Write Python programs to count the number of vowels in a sentence input by the user.
sentence=(input('ENTER ANY SENTENCE:'))
count=0
for i in sentence:
    if i in 'aeiou':
        count+=1
print(count)
        
    
