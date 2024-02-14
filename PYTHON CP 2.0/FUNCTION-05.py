# Write a function which takes as input a file name and a list of values and write the list of values to the specified file. If
# the file already exists then the new values are appended to it.
def write_to_file(filename,lst):
    f=open(filename,'a')
    for i in lst:
        f.write(str(i)+' ')
    f.close()
write_to_file('values.txt',[1,2,3])
write_to_file('values.txt',[4,5,6])