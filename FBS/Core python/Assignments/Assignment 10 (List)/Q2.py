### Q2. Write a program to find maximum and minimum element in a list ?

def find_max_min(li):
    max = li[0]
    min = li[0]

    for ind in range (1, len(li)):
        if (li[ind] < max):
            max = li[ind]
        
        if (li[ind] > min):
            min = li[ind]
        
    return max, min

li = [10, 20, 40, 30, 50]

max, min = find_max_min(li)

print("Maximum element :", max)
print("Minimum element :", min)