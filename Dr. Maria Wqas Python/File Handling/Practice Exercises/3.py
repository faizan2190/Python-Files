# Write a function fcopy that takes as input two file names (as strings) and copies the content of the first file into the
# second line by line.
def fcopy(file1,file2):
    with open(file1) as file1:
        content=file1.read()
    with open(file2,'w') as file2:
        file2.write(content)
fcopy('censored.txt','f.copy.txt')