# We can represent a Tic-Tac-Toe board as a 3 x 3 grid in which each position can hold one of the following three
# strings: "X", "O", or " ". Write code that inputs a 3 x 3 list from user. If "X" appears in a winning Tic-Tac-Toe pattern,
# print "X". If "O" appears in a winning Tic-Tac-Toe pattern, print "O". If no winning pattern exists, the function should
# return the string " ".
for i in range(3):
    lst=input('Enter the row of list deparated ny space')
    lst=lst.split()
