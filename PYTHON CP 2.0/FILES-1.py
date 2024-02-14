with open('pass.txt','a+') as file:
    file.write('Owais Madani\n')
    file.seek(0)
    print(file.read())

