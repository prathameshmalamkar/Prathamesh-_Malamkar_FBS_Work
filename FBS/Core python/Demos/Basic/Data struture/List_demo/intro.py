#1. Structure : Denoted by []

li = [10, 30, 20, 40]
print(type(li))

#2. Type of data : Heterogeneous

li = [10, 3.14, 'abc']
print(li)

#3. sequence : Ordered


#4. changeable : Mutable

print(id(li))
li[1] = 17.63
print(id(li))
print(li)

#5. Duplication : Allowed

li = [10, 10, 20, 30, 20, 10]
print(li)