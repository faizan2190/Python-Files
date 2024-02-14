# Write a function selected_prime that prints all the prime numbers less than 1,000 that contain the digit 2 or digit
# 3 (or both). Organize your code to use two functions: the first one takes an integer as argument, returns True if the
# number is prime and False otherwise; the second function returns True if an integer contains the digits 2 or 3 or both,
# and False otherwise.
def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
def is2or3include(n):
    if '2' in str(n) or '3' in str(n):
        return True
    else:
        return False
def selected_prime():
    for i in range(1,1001):
        if is_prime(i) and is2or3include(i):
            print(i)
selected_prime()

