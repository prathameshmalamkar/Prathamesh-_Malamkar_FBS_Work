li = [40, 20, 10, 30]

#1. append () - Adds one element at the end of the list.
li.append(50)
print(li)

#2. clear () - Remove all element from the list.
# li.clear()
# print(li)

#3. copy () - Create and returns a copy of the list.
li2 = li.copy()
print(li2)

#4. count() - Returns the number of times an element appears.
print(li.count(30))


#5. extend() - Adds all elements of another list to the end.
li.extend([80, 90, 100])
print(li)

#6. index() - Returns the index of the first matching element.
li.index(40)
print(li)

#7. insert() - Inserts an element at a specific index.
li.insert(2,70)
print(li)

#8. pop() - Removes and returns the element at the given index (last by default).
li.pop(1)
print(li)

#9. remove() - Removes the first matching element from the list.
li.remove(50)
print(li)

#10. reverse() - Reverses the order of the list.
li.reverse()
print(li)

#11. sort() - Sorts the list in ascending order (default).
li.sort(reverse=True)
print(li)



