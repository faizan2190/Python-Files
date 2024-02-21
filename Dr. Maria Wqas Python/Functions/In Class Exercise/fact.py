# Find the factorial of a number using recursion...
def fact(n):
    n=int(input("Enter an integer for factorial:"))
    for i in range(len(n)):
        if n!=1:
            fact(n-1)
