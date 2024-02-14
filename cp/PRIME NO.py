def prime(i):
    count=0
    for j in range(1,i+1):
        if i % j==0:
            count+=1
    if count==2:
        return True
    else:
        return False
def is23(i):
    if '2' in str(i) or '3'in str(i):
        return True
    else:
        return False
def selected_prime():
    for i in range(1,1001):
        if prime(i) and is23(i):
            print(i)
selected_prime()