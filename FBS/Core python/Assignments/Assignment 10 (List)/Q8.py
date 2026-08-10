### Q8. Write a program to create a duplicate of an existing list. It should not point to same list ?

def dupli_list(li):
    new = []

    for val in li:
        new = new + [val]
        
    return new

li = [10, 20, 30, 40, 50]

res = dupli_list(li)
    
print(f"Original list :", li)
print(f"Duplicate list :", res)