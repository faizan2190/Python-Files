value=input('enter the values separated by spaces:')
value=value.split()
file=open('data.txt','a')
for i in value:
    file.write(i+',')
file.close()