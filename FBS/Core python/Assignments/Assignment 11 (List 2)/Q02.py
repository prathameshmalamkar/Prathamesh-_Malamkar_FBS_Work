### Q2. Python Program to Merge Two Lists and Sort it ?

def marge_sort(li1, li2):
    
    new_li = li1 + li2
    new_li.sort()
    
    return new_li

li1 = [5, 7, 9]
li2 = [3, 4, 8]

res = marge_sort(li1, li2)

print(f"Marge and sort list :", res)