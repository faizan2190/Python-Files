#produce a code to get first second best score from the list
#l=[86,86,85,85,85,83,23,45,84,1,2,0]
gadget=['mobile','laptop',100,'camera',310.28,'speaker',27.00,'television',1000,'laptop case','camera lens']
#list of numr:
string=[]
num=[]
for i in gadget:
    if type(i) == int or type(i) == float:
        num.append(i)
    else:
        string.append(i)

print(num)
print(string)