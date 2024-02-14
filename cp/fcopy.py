# Write a function fcopy that takes as input two file names (as strings) and copies the content of the first file into the
# second line by line.
def fcopy(copyfrom,copyto):
    file=open(copyfrom,'r+')
    content=file.readlines()
    file.close()
    file2=open(copyto,'w')
    file2.writelines(content)
    file2.close()
copyfrom=input('enter the file name')
copyto=input('enter the file name')
fcopy(copyfrom,copyto)