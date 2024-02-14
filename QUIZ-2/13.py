# Print contents of a large file on screen. Do not read the whole file at once; read it line by line and print each line
# removing the next line character.
file=open('new.txt','r')
for i in file:
    x=i.strip()
    print(x)