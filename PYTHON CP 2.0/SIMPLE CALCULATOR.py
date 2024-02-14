#SIMPLE CALCULATOR
def calc(choice):
    if choice==1:
        def addition(a,b):
            return a+b
        print(addition(a,b))
    if choice == 2:
        def subtraction(a,b):
            return a-b
        print(subtraction(a,b))
    if choice == 3:
        def multiplication(a,b):
            return a*b
        print(multiplication(a,b))
    if choice == 4:
        def division(a,b):
            return a/b
        print(division(a,b))
menu=print('1-addition\n2-subtraction\n3-multiplication\n4-division')
choice=int(input('ENTER YOUR CHOICE:'))
a=int(input('enter a number-1:'))
b=int(input('enter a number-2:'))
calc(choice)