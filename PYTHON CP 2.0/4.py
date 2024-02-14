values=input('enter a non negative integer seperated by space:')
values=values.split()
f=open('val.txt','w+')
for val in values:
    if val.isdigit():
        f.write(val+' ')
choice =input("press 'y' if you want to see the list:")
if choice=='y':
    f.seek(0)
    print(f.read())
f.close()