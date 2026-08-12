s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
s3 = {50, 60}

#1. add() - Add an element to the set
s1.add(50)
print(s1)

#2. clear()  Remove all element from the set
# s1.clear()
# print(s1)

#3. copy() - REturn a copy of the set
s4 = s1.copy()
print(s4)

#4. difference() - Return element present in the first set but not in the second
print(s1.difference(s2))

#5. difference_update() - Remove element that are present in another set
s1.difference_update(s2)
print(s1)

#6. discard() - Removes a specified element without giving an error if not found
s1.discard(40)
print(s1)

#7. intersection() - Return common element from both sets
print(s1.intersection(s2))

#8. intersection_update() - Keeps only common element in the set
s1.intersection_update(s2)
print(s1)

#9. isdisjoint() - Check whether two sets have no common element
print(s1.isdisjoint(s3))

#10. issubset() - Check whether one set is a subset of another
print(s3.issubset(s2))

#11. issuperset() - Check whether one set is a superset of another
print(s2.issuperset(s3))

#12. pop() - Remove and return an arbitrary element
#print(s1.pop())

#13. remove() - Remove a specified element , given an error if not found
# s1.remove(20)
# print(s1)

#14. symmetric_difference() - Return element that are not common in both sets
print(s1.symmetric_difference(s2))

#15. symmetric_difference_update() - Update the set with non-common element 
s1.symmetric_difference_update(s2)
print(s1)

#16. union() - Return all element from both sets
print(s1.union(s2))

#17. update() - Adds multiple element to the set
s1.update({70,80,90})
print(s3)
