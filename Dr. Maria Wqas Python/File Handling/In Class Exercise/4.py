# Write Python program to input and store non-negative integer values from user. User can input as many values as
# s/he wants separated by spaces; presses enter to quit. Ignore any other invalid entries; do not write them to file. Ask
# user if s/he wants to see the contents of the file at the end.
with open('text.txt','w') as file:
    num=input('enter a values separated by spaces:')
    num=num.split()
    # num=[int(i) for i in num]
    for i in num:
        if i.isdigit():
            file.write(i+' ')
n=input('enter"v" if you want to check the entry:')
if n=='v':
    with open('text.txt') as file:
        for line in file:
            print(line)
