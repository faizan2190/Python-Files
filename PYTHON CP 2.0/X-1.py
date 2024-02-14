# # # # Write a function to count and return negative values in a list. The list is passed as argument to the function.
# # #
# # # # def neg_lst(l):
# # # #     count = 0
# # # #     neglst=[]
# # # #     for i in l:
# # # #         if i<0:
# # # #             count+=1
# # # #             neglst.append(i)
# # # #     return(count,neglst)
# # # # l1=[1,-4,3,-5]
# # # # x=neg_lst(l1)
# # # # print(x[0])
# # # # print(x[1])
# # # # Write code that inputs a list and a value. If the value is present in the list it returns the index of its first occurrence,
# # # # otherwise returns a None. In the main program use this return value to print appropriate messages. Do not call any
# # # # method of object list.
# # # def index(lst,val):
# # #     for i in range(len(lst)):
# # #         if lst[i]==val:
# # #             return (i)
# # # l=[1,2,3,4,5,6]
# # # value=5
# # # x=index(l,value)
# # # print(x)
# # #
# # #
# # # Write a function to input a list of integers from the user. The function returns the list to the caller.
# # def lst():
# #     value=input('enter the values separated by spaces:')
# #     value=value.split()
# #     value=[int(i) for i in value]
# #     return value
# # x=lst()
# # print(x)
# # Write a function to input a list of integers from the user. The function receives an empty list from user.
# def lst(l):
#
#     value=input('enter values seperated by spaces:')
#     value=value.split()
#     value=[int(i) for i in value]
#
# l=[]
# lst(l)
# print(l)
def g(x):
    x=4
x=3
g(x)
print(x)
pri