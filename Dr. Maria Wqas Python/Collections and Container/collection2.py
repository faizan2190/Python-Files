# Write code that counts and prints the even numbers in a list of integers. For example, a list containing the elements
# 3;5;4;-1; and 0, would evaluate to 2, since there are only two even numbers: 4 and 0. The code prints zero if the list is
# empty.
l=[3,5,4,-1,0]
#l=0
count=0
total=0
if len(l)>0:
    for i in l:
        if i%2 == 0:
            count+=1
            print(i,end=',')
    print()
    print(f'Total even number s are {count}')
else:
    print('zero')