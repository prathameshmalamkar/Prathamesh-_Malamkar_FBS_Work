### Q1. Write a Python program to find elements in a given set that are not in another set.

def find_difference (set1, set2):
    return set1 - set2

s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}

res = find_difference (s1, s2)

print(f"Element in s1 but not s2 :", res)