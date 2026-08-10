### Q13. Write a program to print list after removing even numbers ?

def remove_even(li):
    
    new = []
    
    for i in li :
        if i % 2 != 0 :
            new = new + [i]
            
    return new

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = remove_even(li)

print(f"The original list :", li)
print(f"The after removing even numbers :", res)