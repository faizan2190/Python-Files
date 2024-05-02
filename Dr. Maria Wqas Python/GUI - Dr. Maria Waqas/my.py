l = []

for i in range(int(input())):
    l1 = []
    name = input()
    score = input()
    l1.append(name)
    l1.append(score)
    l.append(l1)

scorelist = []
for i in l:
    scorelist.append(i[1])
scorelist.sort()

num = scorelist[0]
for i in scorelist:
    if i == num:
        scorelist.pop(0)

ans = []
for j in l:
    if scorelist[0] == j[1]:
        ans.append(l[0])
print(ans)

