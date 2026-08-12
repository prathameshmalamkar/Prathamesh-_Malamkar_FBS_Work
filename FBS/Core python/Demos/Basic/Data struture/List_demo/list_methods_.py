li = [40, 20, 10, 30]

li.append(50)
print(li)

li.clear()
print(li)

li2 = li.copy()
print(li)

li3 = li
li.append(50)

print(li.count(30))

li.extend([80, 90, 100])
print(li)

print(li.index(50))
print(li)

li.insert(2,70)
print(li)

li.pop(1)
print(li)

li.remove(50)
print(li)

li.reverse()
print(li)

li.sort(reverse=True)
print(li)