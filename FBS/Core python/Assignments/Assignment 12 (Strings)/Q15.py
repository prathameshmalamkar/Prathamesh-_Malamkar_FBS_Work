### Q15. Python Program to find larger string without using built-in functions.

def larger_string(str1, str2):
    count1 = 0
    count2 = 0

    for i in str1:
        count1 = count1 + 1

    for i in str2:
        count2 = count2 + 1

    if count1 > count2:
        return str1
    elif count2 > count1:
        return str2
    else:
        return "Both strings are equal"


p = input("Enter first string: ")
q = input("Enter second string: ")

res = larger_string(p,q)

print("Larger string:", larger_string(p,q))