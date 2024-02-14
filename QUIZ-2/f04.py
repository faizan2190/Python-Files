# Write Python program to input and store non-negative integer values from user. User can input as many values as
# s/he wants separated by spaces; presses enter to quit. Ignore any other invalid entries; do not write them to file. Ask
# user if s/he wants to see the contents of the file at the end.
f=open('file2.txt','a+')
num=input('enter non negative integers separated by spaces:')
num=num.split()
num=[int(i) for i in num]
for i in num:
    if i<0:
        f.write(str(i)+' ')
f.close()
f=open('file2.txt','r')
check=input('enter "v" to check the entry:')
if check=='v':
    for i in f:
        print(i)
else:
    print('thank you')
f.close()
