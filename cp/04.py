# Write Python program to input and store non-negative integer values from user. User can input as many values as
# s/he wants separated by spaces; presses enter to quit. Ignore any other invalid entries; do not write them to file. Ask
# user if s/he wants to see the contents of the file at the end.
integer=input('enter integers separated by spaces:')
integer=integer.split()
file=open('newfile.txt','w+')
for i in integer:
    if i.isdigit():
        file.write(i+' ')
check=input('enter "v" if you want to check the entry:')
if check=='v':
    file.seek(0)
    print(file.read())
