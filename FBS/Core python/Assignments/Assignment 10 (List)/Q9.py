### Q9. Write a program of having n number of elements in the list and find out even and
### odd elements in that list and then create two separate lists which will have even elements and
### other will have odd elements ?

def even_odd(li):
    even = []
    odd = []

    for val in li :
        if val % 2 == 0 :
            even = even + [val]
        else :
            odd = odd + [val]
            
    return even, odd

li = [10, 15, 20, 25, 30, 35, 40, 45]

even, odd = even_odd(li)
        
print(f"It is even numbers :" , even)
print(f"It is odd numbers :", odd)