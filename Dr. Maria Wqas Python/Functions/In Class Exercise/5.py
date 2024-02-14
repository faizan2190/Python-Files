# Write a function which takes as input a file name and a list of values and write the list of values to the specified file. If
# the file already exists then the new values are appended to it.
def write_to_file(filename,lst):
    with open(filename,'a') as file:
        for i in lst:
            file.write(str(i)+' ')
write_to_file('mytext.txt',[1,2,3,4,5])