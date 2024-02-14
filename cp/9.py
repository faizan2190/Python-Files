# Write code that counts and prints the even numbers in a list of integers. For example, a list containing the elements
# 3;5;4;-1; and 0, would evaluate to 2, since there are only two even numbers: 4 and 0. The code prints zero if the list is
# empty.
count=0
even_lst=[]
lst=[3,5,4,-1,0]
for i in lst:
    if i % 2==0:
        count+=1
        even_lst.append(i)
print(f'The even number list is {even_lst}')
print(f'The even number in a list is {count}')