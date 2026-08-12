s1 = frozenset({10, 20, 30, 40})
s2 = frozenset({30, 40, 50})

#1. s1.copy() - Return a copY of  the frozenset
s3 = s1.copy()
print(s3)

#2. s1.difference() - Return element present in s1 but in s2
print(s1.difference(s2))

#3. intersection() - Return common element from both frozenset
print(s1.intersection(s2))

#4. isdisjoint() - Return True if no common element are present
print(s1.isdisjoint(s2))

#5. issubset() - Check whether s1 is a subset of s2
print(s1.issubset(s2))

#6. issuperset() - Check whether s1 is a superset of s2
print(s1.issuperset(s2))

#7. symmetric_difference() - Return non-common element from both frozenset
print(s1.symmetric_difference(s2))

#8. union() - Return all element from both frozenset
print(s1.union(s2))