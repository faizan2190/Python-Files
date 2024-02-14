# Write Python program to input and store non-negative integer values from user. User can input as many values as
# s/he wants separated by spaces; presses enter to quit. Ignore any other invalid entries; do not write them to file. Ask
# user if s/he wants to see the contents of the file at the end.
value=input('enter the values separated by spaces:')
value=value.split()
file=open('data.txt','w+')
for i in value:
    file.write(i+' ')
check=input('enter v to check entery:')
if check=='v':
    file.seek(0)
    print(file.read())