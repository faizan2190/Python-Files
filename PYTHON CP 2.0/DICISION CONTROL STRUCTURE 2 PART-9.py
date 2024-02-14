##12. Write a Python program to input marks (obtained marks as well as maximum marks) for five subjects Physics,
##Chemistry, Biology, Mathematics and Computer. It calculates and prints percentage and grade according to following:
##Percentage >= 90% : Grade A
##Percentage >= 80% : Grade B
##Percentage >= 70% : Grade C
##Percentage >= 60% : Grade D
##Percentage >= 40% : Grade E
##Percentage < 40% : Grade F
PhyObt=int(input('ENTER PHYSICS OBTAINED MARKS:'))
PhyMax=int(input('ENTER PHYSICS MAX MARKS:'))
ChemObt=int(input('ENTER CHEMISTRY OBTAINED MARKS:'))
ChemMax=int(input('ENTER CHEMISTRY MAX MARKS:'))
BioObt=int(input('ENTER BIOLOGY OBTAINED MARKS:'))
BioMax=int(input('ENTER BIOLOGY MAX MARKS:'))
MathsObt=int(input('ENTER MATHEMATICS OBTAINED MARKS:'))
MathsMax=int(input('ENTER MATHEMATICS MAX MARKS:'))
ComObt=int(input('ENTER COMPUTER OBTAINED MARKS:'))
ComMax=int(input('ENTER COMPUTER MAX MARKS:'))
var1=PhyObt+ChemObt+BioObt+MathsObt+ComObt
var2=PhyMax+ChemMax+BioMax+MathsMax+ComMax
Percentage=(var1/var2)*100
if Percentage >= 90:
    print('GRADE-A')
elif 90>Percentage>=80:
    print('GRADE-B')
elif 80>Percentage>=70:
    print('GRADE-C')
elif 70>Percentage>=60:
    print('GRADE-D')
elif 70>Percentage>=40:
    print('GRADE-E')
else:
    print('GRADE-F')
