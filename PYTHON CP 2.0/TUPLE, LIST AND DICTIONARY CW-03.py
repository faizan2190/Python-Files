#input multiterm word and print acronium
acr=''
term=input('enter a multiword term:')
term=term.split()
for i in range(len(term)):
    acr+=term[i][0].upper()
print(acr)
#OR
#for i in term:
#acr+=i[0].upper()