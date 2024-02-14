##Write a Python program that requests five integer values from the user. It then prints the maximum and minimum
##values entered. If the user enters the values 3, 2, 5, 0, and 1, the program would indicate that 5 is the maximum and 0
##is the minimum. Your program should handle ties properly; for example, if the user enters 2, 4, 2, 3, and 3, the
##program should report 2 as the minimum and 4 as maximum.
val1=int(input('ENTER AN INTEGER:'))
val2=int(input('ENTER AN INTEGER:'))
val3=int(input('ENTER AN INTEGER:'))
val4=int(input('ENTER AN INTEGER:'))
val5=int(input('ENTER AN INTEGER:'))

a=min(val1,val2,val3,val4,val5)
print(a,'is min')
b=max(val1,val2,val3,val4,val5)
print(b,'is max')

