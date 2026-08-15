### Q7. Python Program to Remove the Given Key from a Dictionary.

def remove_key(dict, key):
    dict.pop(key)
    
    return dict

dict1 = {'a': 30, 'b': 50, 'c': 70, 'd': 90}

p = input("Enter a remove key :")

res = remove_key(dict1, p)

print(f"After removing key in dictionary :", res)
