d={}
while True:
    roll=input('enter roll number')
    if roll=='q' or roll=='Q':
        break
    name=input('enter your name')
    d[roll]=name
print(d)
