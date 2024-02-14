gadget=['mobile','laptop',100,'camera',310.28,'speaker',27.00,'television',1000,'laptop case','camera lens']
#list of string and numbers:
string=[gadget[0],gadget[1],gadget[3],gadget[5],gadget[7],gadget[9],gadget[10]]
num=[gadget[2],gadget[4],gadget[6]]
print(string)
print(num)
#sort the string list:
string.sort()
print(string)
string.sort(reverse=True)
print(string)
num.sort()
print(num)
num.sort(reverse=True)
print(num)