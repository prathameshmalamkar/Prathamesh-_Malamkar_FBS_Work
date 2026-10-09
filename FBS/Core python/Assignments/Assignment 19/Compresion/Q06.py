### Q06. Use a dictionary comprehension to count the length of each word in a sentence (take input from user)

str =input("enter a string:")
di={word : len(word) for word in str.split()}
print(di)