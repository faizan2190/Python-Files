#ENTER 5 INTEGER SEPERATED BY SPACE AND PLACE THEM IN A LIST...
val=input('enter 5 integer seperated by space:')
val=val.split()
for i in range(len(val)):
    val[i]=int(val[i])
print(val)
# or
val=[int(i) for i in val]