### Q1. Python Program to Put Even and Odd elements of a List into two Different lists ?

def even_odd(li):
    even_list = []
    odd_list = []
    
    for num in li :
        if num % 2 == 0 :
            even_list.append(num)
        else :
            odd_list.append(num)
            
    return even_list, odd_list
            
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even, odd = even_odd(li)

print(f"The even number of list :", even)
print(f"The odd number of list :", odd)
        