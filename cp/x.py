def is_prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
def contain_2or3(x):
    if '2' in str(x) or '3' in str(x):
        return True
    else:
        return False

def selected_prime():
    for i in range(1,1001):
        if is_prime(i) and contain_2or3(i):
            print(i)
selected_prime()