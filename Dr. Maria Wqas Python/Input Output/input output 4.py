# Input first and last name from user, print initials in all caps on screen. For example, if the user enters ‘Mark Lutz’, print
# ‘M.L.’
first_name=input('enter your first name:')
last_name=input('enter your last name:')
print(f'{first_name[0].upper()}.{last_name[0].upper()}')