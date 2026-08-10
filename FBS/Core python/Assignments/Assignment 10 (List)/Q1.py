#### Q1.Write a program to find sum of all elements of list ?

def sum_list(li):
    total = 0

    for i in (li):
    
        total += i
        
    return total
li = [10, 20, 30, 40, 50]

res = sum_list(li)
    
print(res)