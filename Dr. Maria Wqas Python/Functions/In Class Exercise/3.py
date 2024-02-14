def func():
    val=input('Enter values seaparated by space')
    val=val.split()
    val=[int(i) for i in val]
    return val
print(func())
