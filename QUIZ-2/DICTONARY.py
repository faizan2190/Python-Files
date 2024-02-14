#write a code to input roll no as key and name as value:
#input -ve no to exit
d={}
while True:
    print("enter 'q' for terminate")
    roll=input('enter roll number:')
    if roll=='q':
        break
    name = input('enter name:')
    d.update({roll:name})
print(d)