# The function censor takes the name of a file (a string) as input. The function should open the file, read it, and then
# write it into file censored.txt with this modification: Every occurrence of a four-letter word in the file should be
# replaced with string 'xxxx'. Note that this function produces no output, but it does create file censored.txt in the
# current folder.
def censor(filename):
    file=open(filename,'r+')
    content=file.read()
    words=content.split()
    file.seek(0)
    for i in words:
        if len(i)==4:
            file.write('xxxxx'+' ')

filename=input('enter the filename:')
x=censor(filename)
