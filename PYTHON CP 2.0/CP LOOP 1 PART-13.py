##Repeat problem 12, now allowing user to enter a many integers as he/she wants to. The user enters a negative number
##to terminate.
total=0
count=0
while True:
    


    num=int(input('ENTER POSITIVE INTEGER:'))
    if num>0:

        count+=1
        total+=num

    else:
        break
print(total/count)
    
