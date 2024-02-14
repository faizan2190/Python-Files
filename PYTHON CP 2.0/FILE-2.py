f=open('myfile.txt')
text=f.read()
print(len(text))
word=text.split()
print(len(word))
lines=text.split('\n')
print(len(lines))
alphabets=0
for i in text:
    if i.isalpha():
        alphabets+=1
print(alphabets)
f.close()
