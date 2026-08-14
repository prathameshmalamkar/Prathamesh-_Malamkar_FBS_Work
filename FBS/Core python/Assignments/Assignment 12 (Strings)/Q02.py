### Q2. Python Program to Remove the nth Index Character from a Non-Empty Strings ?

def remove_char(s, n):
    return s[:n] + s[n+1:]

a = input("Enter string: ")
b = (input("Enter index: "))

print("String after removing character:", remove_char(a, b))
    