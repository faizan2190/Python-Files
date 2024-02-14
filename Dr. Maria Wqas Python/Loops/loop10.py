# Write Python programs to count the number of vowels in a sentence input by the user.
sen=input('enter the sentence:')
count=0
for i in range(len(sen)):
    if sen[i]=='a' or sen[i]=='e' or sen[i]=='i' or sen[i]=='o' or sen[i]=='u':
        count+=1
print(f'The number of vowels are {count}')