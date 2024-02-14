# Write Python program to input and store non-negative integer values from user. User can input as many values as
# s/he wants separated by spaces; presses enter to quit. Ignore any other invalid entries; do not write them to file. Ask
# user if s/he wants to see the contents of the file at the end.
integer=input('enter integers separated by spaces:')
integer=integer.split()
integer=[int(i) for i in integer]
file=open('newfile.txt','w')
for i in integer:
    file.write(str(i)+' ')
file.close()
file=open('newfile.txt')
file=file.read()
total=0
count=0
for i in file:
    if i.isdigit():
        count+=1
        total+=int(i)
x=total/count
print(x)
print(total)
print(count)