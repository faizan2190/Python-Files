# Print contents of a large file on screen. Do not read the whole file at once; read it line by line and print each line
# removing the next line character.
f=open('file.txt')
for line in f:
    print(line.strip())