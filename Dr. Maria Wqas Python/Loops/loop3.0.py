l=[]
count=0
while True:
    n=float(input('enter the non negative integer:'))
    if n<0:
        break
    else:
        l.append(n)
        count+=1
print(sum(l))
print(max(l))
print(min(l))
print(sum(l)/count)