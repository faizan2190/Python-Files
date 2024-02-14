#GIVE THE POSSIBLE IMPLEMENTATION OF SPLIT FUNCTION
chunk=''
l=[]
sen=input('enter any sentence:')
for i in sen:
    if i!=' ':
        chunk+=i
    else:
        l+=[chunk]
        chunk=''
if chunk!='':
    l+=[chunk]
print(l)