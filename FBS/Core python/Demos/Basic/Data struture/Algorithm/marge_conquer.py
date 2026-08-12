def conquer (li, start, mid, stop):
    left = start
    right = mid + 1
    temp = []
    while left <= mid and right <= stop:
        if li [left] < li [right]:
            temp.append (li[left])
            left += 1
        else:
           temp.append (li[right])
           right += 1 
         
    while left <= mid :
        temp.append (li[left])
        left += 1
    
    while right <= mid :
            temp.append (li[right])
            right += 1
            
    for i in range (len(temp)):
        li[start + i] = temp [i]
        
def divide (li, start, stop):
    if stop > start :
        mid = ( start + stop)//2
        divide (li, start, mid)
        divide (li, mid + 1, stop)
        conquer (li, start, mid, stop)
        
li = [50, 14, 18, 12, 1, 96]

print (f"Before sorting = {li}.")

divide (li, 0, len(li)- 1 )

print (f"After sorting = {li}.")



            
        
    
        