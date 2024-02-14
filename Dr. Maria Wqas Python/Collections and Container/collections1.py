# Write code to add up and print all the positive values in a list of integers. For example, a list containing the elements
# [3,-3,5,2,-1,2] would evaluate to 12, since 3+5+2+2 = 12. The code prints zero if the list is empty.
lst=[]
# lst=[3,-3,5,2,-1,2]
total=0
if len(lst)>0:
    for i in lst:
        if i > 0:
            total+=i
    
    print(f'The sum of all positive in the list is {total}')
else:
    print('zero')