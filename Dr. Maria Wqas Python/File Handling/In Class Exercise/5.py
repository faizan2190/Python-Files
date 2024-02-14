# Write Python program to read the file created in last example and print average of the numbers.
with open('text.txt','r') as file:
    total=0
    count=0
    content=file.read()
    for i in content:

        if i.isdigit():
            total+=int(i)
            count+=1
    print(total/count)  