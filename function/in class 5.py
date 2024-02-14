# Write a function which takes as input a file name and a list of values and write the list of values to the specified file. If
# the file already exists then the new values are appended to it.
def file(filename,lst):
    f=open(filename,'a')
    for i in lst:
        f.write(str(i)+' ')
file('data.txt',[1,2,3,4])