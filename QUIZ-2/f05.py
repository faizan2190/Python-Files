# Write Python program to read the file created in last example and print average of the numbers.
f=open('file2.txt')
f=f.read()
f=f.split()
f=[int(i) for i in f]
total=0
count=0
for i in f:
    total+=i
    count+=1
print(total/count)