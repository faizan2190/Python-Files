#Write a Python program to input basic salary of n employees; calculate and print the gross and net salary according to
#following rules. The value n should also be taken from user at the start of the program.
#Gross Salary = Basic Salary (BS) + House Rent Allowance (HRA) + Dearness Allowance (DA)
#Net Salary = Gross Salary (GS) – Deductions (DD)
#BS <= 10000 : HRA = 20% of BS, DA = 80% of BS, DD = 2% of BS
#BS <= 20000 : HRA = 25% of BS, DA = 90% of BS, DD = 4% of BS
#BS > 20000 : HRA = 30% of BS, DA = 95% of BS, DD = 10% of
n=int(input('enter the no. of employee:'))
for i in range(1,n+1):
    employeesalary=int(input('enter a basic salary of employe')):
    if employeesalary <=10000:
        gs=employeesalary + 0.2+0.8
        ns=gs-0.02
    elif 10000<= employeesalary <= 20000:
        gs = employeesalary + (25/100) + (0.9)
        ns = gs - 0.04
    elif employeesalary > 20000:
        gs = employeesalary + 0.3 + 0.95
        ns = gs - 0.1
    else:
        print('error')
if employeesalary>0:
    print(gs)
    print(ns)