# Implement a program that requests four numbers (integer or floating-point) from the user. Your program should
# compute the average of the first three numbers and compare the average to the fourth number. If they are equal, your
# program should print 'Equal' on the screen.
# Test Data:
# Enter number 1: 4.5
# Enter number 2: 3
# Enter number 2: 3
# Enter last number: 3.5
# Expected Output: Equal
sum=0
for i in range(3):
    val=int(input('Enter the number'))
    sum+=val
ave=sum/3
val1=int(input('Enter the number'))
if ave==val1:
    print('equal')
