# We can represent a Tic-Tac-Toe board as a 3 x 3 grid in which each position can hold one of the following three
# strings: "X", "O", or " ". Write code that inputs a 3 x 3 list from user. If "X" appears in a winning Tic-Tac-Toe pattern,
# print "X". If "O" appears in a winning Tic-Tac-Toe pattern, print "O". If no winning pattern exists, the function should
# return the string " ".

lst=[]
for i in range(3):
    l1=[]
    for j in range(3):
        x=input('Enter "X" or "O"')
        l1.append(x)
    lst.append(l1)
for i in range(len(lst)):
    for j in range(len(lst)):
        print(lst[i][j],end=' ')
    print()
print()
if (lst[0][0]=='X' and lst[0][1]=='X' and lst[0][2]=='X') or (lst[1][0]=='X' and lst[1][1]=='X' and lst[1][2]=='X') or (lst[2][0]=='X' and lst[2][1]=='X' and lst[2][2]=='X') or (lst[0][0]=='X' and lst[1][0]=='X' and lst[2][0]=='X') or (lst[0][1]=='X' and lst[1][1]=='X' and lst[2][1]=='X') or (lst[0][2]=='X' and lst[1][2]=='X' and lst[2][2]=='X')or (lst[0][0]=='X' and lst[1][1]=='X' and lst[2][2]=='X') or (lst[0][2]=='X' and lst[1][1]=='X' and lst[2][0]=='X'):
    print('X WINS')
elif (lst[0][0]=='O' and lst[0][1]=='O' and lst[0][2]=='O') or (lst[1][0]=='O' and lst[1][1]=='O' and lst[1][2]=='O') or (lst[2][0]=='O' and lst[2][1]=='O' and lst[2][2]=='O') or (lst[0][0]=='O' and lst[1][0]=='O' and lst[2][0]=='O') or (lst[0][1]=='O' and lst[1][1]=='O' and lst[2][1]=='O') or (lst[0][2]=='O' and lst[1][2]=='O' and lst[2][2]=='O')or (lst[0][0]=='O' and lst[1][1]=='O' and lst[2][2]=='O') or (lst[0][2]=='O' and lst[1][1]=='O' and lst[2][0]=='O'):
    print('O WINS')
else:
    print('TIE')