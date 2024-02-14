# Print contents of a large file on screen. Do not read the whole file at once; read it line by line and print each line
# removing the next line character.
file=open('x.txt')
for line in file:
    print(line.strip())
