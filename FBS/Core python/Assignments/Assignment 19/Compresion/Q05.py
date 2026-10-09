### Q05. Find all of the words in a string that are less than 5 letters (take input from user)

str =input("enter the String:")
li=[]
words=""
# for words in str.split():
#     if(len(words)<5):
#         li.append(words)

# print(li)
# using built in function
li=[words for words in str.split() if(len(words)<5) ]
print(li)

# for ch in str:
#     if ch !=" ":
#         words += ch
#     else:
#         if words !=" ":
#             li.append(words)
#         words=" "
# if words !=" ":
#     li.append(words)
# print(li)


    