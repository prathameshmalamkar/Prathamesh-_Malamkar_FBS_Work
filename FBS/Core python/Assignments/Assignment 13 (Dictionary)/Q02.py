### Q2. Python Program to Concatenate Two Dictionaries Into One.

def concatenate_dict(dict1,dict2):
    dict1.update(dict2)
    return dict1

dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

res = concatenate_dict(dict1, dict2)

print(f"The concatenate dictionaries :", res)