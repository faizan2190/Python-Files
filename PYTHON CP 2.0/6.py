integer=input('enter an integer seperated by space:')
integer=integer.split()
print(integer)
f=open('integer.txt','w')
for i in f:
    f.write(integer+' ')
f.close()


