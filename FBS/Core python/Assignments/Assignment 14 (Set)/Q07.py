### Q7. Given two sets of numbers, write a Python program to find the missing
### numbers in the second set as compared to the first and vice versa. Use the Python set.

def find_missing (set1, set2):
    return set1 - set2

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7,}

res = find_missing (s1, s2)

print(f"Missing in First Set :", s2 - s1)
print(f"Missing in Second Set :", s1 - s2)