# Write Python program to find sum of n natural numbers. n should be entered by the user.
n=int(input('enter the number of terms:'))
total=0
for i in range(1,n+1):
    total+=i
print('The sum of the given numbers are',total)