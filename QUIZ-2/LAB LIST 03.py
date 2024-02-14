#produce a code to get first second best score from the list
#l=[86,86,85,85,85,83,23,45,84,1,2,0]
l=[86,86,85,85,85,83,23,45,84,1,2,0]
l1=[]
best_score=l[0]

for i in l:
    if i >= best_score:
        best_score=i
    else:
        l1.append(i)
sec_best_score=l1[0]
for j in l1:
    if j >= sec_best_score:
        sec_best_score=j
print('best score is',best_score)
print('second best score is',sec_best_score)


