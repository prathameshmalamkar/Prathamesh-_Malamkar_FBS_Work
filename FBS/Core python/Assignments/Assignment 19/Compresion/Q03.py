### Q03. Count the number of spaces in a string (take input from user)

s = input("enter the String:")
# count =0
# for i in s:
#     if(i ==" "):
#         count+=1
# print(count)

count =[i for i in s if i ==" "]
print(len(count))