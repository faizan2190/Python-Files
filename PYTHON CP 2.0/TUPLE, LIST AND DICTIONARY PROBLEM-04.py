#Write code to take integer inputs from user to form a 3x3 matrix.
l=[]
for i in range(3):
    val=input('enter rows member seperated by space:')
    val=val.split()
    val=[int(i) for i in val]
    l+=[val]
print(l)
#or l.append(val)