### Q10. Write a program to remove all occurrences of a given element in the list ?

def remove_element (li, element) :
    new = []
    
    for val in li :
        if val != element :
            new = new + [val]
            
    return new
            
li = [10, 20, 30, 20, 40, 50]

element = 20

res = remove_element(li, element)
            
print(f"Original list :", li)
print(f"After remove :", res)




