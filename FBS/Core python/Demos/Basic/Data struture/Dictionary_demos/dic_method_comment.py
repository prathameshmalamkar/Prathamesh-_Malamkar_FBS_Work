di = {'id': 101, 'name': 'ABC', 'dept': 'IT'}

#1. di.keys() - Return all the keys from the dict.
di.keys()
print(di)

#2. di.value() - Return all the value from the dict.
di.values()
print(di)

#3. di.items() - Return all the key-value pair.
di.items()
print(di)

#4. di.get() - Return the value of a specified key.
di.get('name')
print(di)

#5. di.update() - Adds new key-value pairs or update exiting value.
di.update({'city': 'pune'})
print(di)

#6. di.pop() - Remove a specified key-value  pair.
di.pop('dept')
print(di)

#7. di.popitem() - Remove the last insert key-value pair.
di.popitem()
print(di)

#8. di.setdefault() - Return the value of a key, if the key does not exist, it adds the key with a default value.
di.setdefault('dept', 'IT')
print(di)

#9. di.copy() - Create a copy of the dict.
di2= di.copy()
print(di2)

#10. di.clear() - Remove all item from the dict.
di.clear()
print(di)

#11. di.fromkeys() - Create a new dict with specified keys and a common value.
di.fromkeys('keys', 'N/A')
print(di)