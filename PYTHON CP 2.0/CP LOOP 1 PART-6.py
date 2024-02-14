##Write a Python program that takes an integer from the user and determines if it is a prime number. Print appropriate
##messages. Prime numbers are those which have only factors: 1 and the number itself.
count=0
integer=int(input('ENTER ANY INTEGER:'))
for i in range(1,integer+1):
    if integer%i==0:
        count+=1
if count==2:
    print('prime')
else:
    print("not prime")
    
