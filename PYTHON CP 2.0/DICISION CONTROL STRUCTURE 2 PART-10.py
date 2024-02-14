##Write a Python program to input basic salary of an employee. It calculates and prints the gross and net salary
##according to following rules.
##Gross Salary = Basic Salary (BS) + House Rent Allowance (HRA) + Dearness Allowance (DA)
##Net Salary = Gross Salary (GS) – Deductions (DD)
##BS <= 10000 : HRA = 20% of BS, DA = 80% of BS, DD = 2% of BS
##BS <= 20000 : HRA = 25% of BS, DA = 90% of BS, DD = 4% of BS
##BS > 20000 : HRA = 30% of BS, DA = 95% of BS, DD = 10% of BS
BS=int(input('ENTER A BASIC SALERY OF EMPLOYEE:'))
if BS<=10000:
    GS=BS+(20/100)+(80/100)
    NS=GS-(2/100)
    print('GROSS SALERY=',GS,'AND NET SALERY=',NS)
elif 10000<BS<=20000:
    GS=BS+(25/100)+(90/100)
    NS=GS-(4/100)
    print('GROSS SALERY=',GS,'AND NET SALERY=',NS)
else:
    GS=BS+(30/100)+(95/100)
    NS=GS-(10/100)
    print('GROSS SALERY=',GS,'AND NET SALERY=',NS)
