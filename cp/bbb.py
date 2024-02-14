def duplicate(filename):
    file=open(filename,'r')
    file=file.read()
    content=file.split()
    x=[]
    for i in content:
        if i in x:
            return True
        x.append(i)
    else:
        return False
n=input('enter file nam')
print(duplicate(n))