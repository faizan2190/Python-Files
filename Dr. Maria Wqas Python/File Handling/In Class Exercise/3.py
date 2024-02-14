# Print contents of a large file on screen. Do not read the whole file at once; read it line by line and print each line
# removing the next line character.
with open('myfile.txt','r') as file:
    for line in file:
        print(line.strip())