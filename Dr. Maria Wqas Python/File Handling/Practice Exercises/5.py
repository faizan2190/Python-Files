# Implement function duplicate that takes as input the name (a string) of a file in the current directory and returns
# True if the file contains duplicate words and False otherwise.
def dupli(filename):
    with open(filename) as file:
        words=[]
        count=0
        content=file.read().split()
        for i in content:
            if i  not in words:
                words.append(i)
            else:
                count+=1
        if count>0:
            return True
        else:
            return False
print(dupli('censored.txt'))
