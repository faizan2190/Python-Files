#factorial
num=int(input('enter a number:'))
def fact(num):
    if not num:
        return 1
    else:
        return num*(fact(num-1))
factorial=fact(num)
print(factorial)