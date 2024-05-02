a=[]
b=[]
n=int(input("Enter number of students: "))

for i in range(n):
    name=input("Enter name: ")
    marks=int(input("Enter marks: "))
    l=[name,marks]
    a.append(l)

for j in range(len(a)):
    count=0
    for k in range(len(a)):
        if a[k][1]<=a[j][1]:
            count+=1
        else:
            count+=0
    if count==2:
        b.append(a[j][0])
    else:
        pass

print(b)
