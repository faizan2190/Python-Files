# The function censor takes the name of a file (a string) as input. The function should open the file, read it, and then
# write it into file censored.txt with this modification: Every occurrence of a four-letter word in the file should be
# replaced with string 'xxxx'. Note that this function produces no output, but it does create file censored.txt in the
# current folder.
def censored(filename):
    with open(filename,'r') as file:
        content=file.read()
        words=content.split()
    with open(filename,'w') as file:
        for word in words:
            if len(word)==4:
                file.write('xxx'+' ')
            else:
                file.write(word+' ')
    print(content)
censored('censored.txt')

