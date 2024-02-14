def censor(filename):
    file=open(filename,'r+')
    content=file.read()
    words=content.split()
    file.seek(0)
    for i in words:
        if len(i)==4:
            file.write('xxx'+' ')
        else:
            file.write(i+' ')
filename=input('enter the file name:')
censor(filename)