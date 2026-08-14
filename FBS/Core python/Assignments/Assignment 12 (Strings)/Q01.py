### Q1. Python Program to Replace all Occurrences of ‘a’ with $ in a Strings ?

def replace_a(s):
    return s.replace('a', '$')

s = input("Enter a string: ")

result = replace_a(s)

print("New string:", result)