### Q2. Write a Python program to remove the intersection of a second set with a first set.

def remove_intersection (set1, set2):
    return set1 - set2

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

res = remove_intersection (s1, s2)

print(f"First set after removing intersection :", res)