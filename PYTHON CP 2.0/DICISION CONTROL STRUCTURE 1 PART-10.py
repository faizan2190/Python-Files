##Write code to find maximum and minimum values among three numbers entered by the user.
num1=int(input('ENTER A NUMBER'))
num2=int(input('ENTER A NUMBER'))
num3=int(input('ENTER A NUMBER'))
if num1>num2 and num2>num3:
    print(num1,'is greater')
elif num3>num2 and num2>num1:
    print(num3,'is greater')
else:
    print(num2,'is greater')
