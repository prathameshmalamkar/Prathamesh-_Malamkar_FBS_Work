### Q7. Write a program to create a new list from existing list which contains cube of each number of list ?

def cube_list(li):
    new = []

    for ind in li :
        cube = ind * ind * ind 
        new = new + [cube]
        
    return new

li = [1, 2, 3, 4, 5]

res = cube_list(li)

print(f"The original list :", li)
print(f"The cube list :", res)
