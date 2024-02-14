# Write a Python program that requests five integer values from the user. It then prints one of two things: if any of the
# values entered are duplicates, it prints "DUPLICATES"; otherwise, it prints "ALL UNIQUE".
count=0
l=[]
l1=[]
for i in range(5):
    num=int(input('enter an integer:'))
    l.append(num)
for i in range(len(l)):
    if l[i] not in l1:
        l1.append(l[i])
    else:
        count+=1
if count>0:
    print('DUPLICATE')
else:
    print('ALL ARE UNIQUE')