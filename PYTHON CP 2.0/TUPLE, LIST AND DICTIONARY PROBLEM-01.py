#Write code to add up and print all the positive values in a list of integers. For example, a list containing the elements
#[3,-3,5,2,-1,2] would evaluate to 12, since 3+5+2+2 = 12. The code prints zero if the list is empty.
lst=[3,4,6,-4,-3,4,-5,2]
lst1=[]
count=0
for i in lst:
    if i>0:
        lst1.append(i)
        count+=i

print(count)
print(lst1)