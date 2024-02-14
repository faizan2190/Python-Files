# Write code to add up and print all the positive values in a list of integers. For example, a list containing the elements
# [3,-3,5,2,-1,2] would evaluate to 12, since 3+5+2+2 = 12. The code prints zero if the list is empty.
lst=[3,-3,5,2,-1,2]
pos_lst=[]
total=0
for i in lst:
    if i>0:
        pos_lst.append(i)
        total+=i
print(pos_lst)
print(f'total of the positive list is {total}')