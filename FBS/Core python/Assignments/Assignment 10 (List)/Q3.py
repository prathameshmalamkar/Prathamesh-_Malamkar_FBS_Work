### Q3. Write a program to find the second largest element in the list ?

def second_largest(li):
    largest = li[0]
    second = li[0]

    for ind in range (1, len (li)):
        if li [ind] > largest:
            second = largest
            largest = li[ind]
        
        elif li > second and li != largest :
            second = li[ind]
            
    return second

li = [10, 20, 40, 50, 60]

res = second_largest(li)
        
print("second largest :", res)