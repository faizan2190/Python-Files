# Write Python program to input and store non-negative integer values from user. User can input as many values as
# s/he wants separated by spaces; presses enter to quit. Ignore any other invalid entries; do not write them to file. Ask
# user if s/he wants to see the contents of the file at the end.
num=input('enter non negative integers seperated by spaces:')
num=num.split()

f=open('new.txt','w+')
for i in num:
    if i.isdigit( ):

        write=f.write(i+' ')
read=input('enter q if you want to see the entry:')
if read=='q':
    f.seek(0)
print(f.read())