### Q5. Python Program to Sum All the Items in a Dictionary.

def sum_item(dict):
    total = 0
    
    for i in dict.values ():
        total = total + i
        
    return total

dict1 = {'a': 10, 'b': 30, 'c': 20, 'd': 50}

res = sum_item(dict1)

print(f"Sum of all Items :", res)