# Write code to find maximum and minimum values among three numbers entered by the user.
l=[]
for i in range(3):
    val=int(input('Enter an integer'))
    l+=val
print(max(l))
print(min(l))