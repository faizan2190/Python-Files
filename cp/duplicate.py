def duplicate(filename):
    file=open(filename,'r')
    content=file.read()
    words=content.split()
    seenword=[]
    for word in content:
        if word in seenword:

            return True
        seenword.append(word)
    else:
        return False
y=input('enter')
print(duplicate(y))