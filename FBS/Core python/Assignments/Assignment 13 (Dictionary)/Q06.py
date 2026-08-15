### Q6. Python Program to Multiply All the Items in a Dictionary.

def mul_item(dict):
    result = 1
    
    for i in dict.values():
        result = result * i
        
    return result

dict1 = {'a': 10, 'b': 5, 'c': 2, 'd': 4}

res = mul_item(dict1)

print(f"The Multiple of Items :", res)