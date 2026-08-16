### Q4. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

def find_pairs (num, target) :
    
    for i in range (len(num)) :
        
        for j in range (i + 1, len(num)) :
            
            if num[i] + num[j] == target :
                
                print(num[i], num[j])


num = [2, 4, 3, 5, 7, 6]

target = 9

find_pairs (num, target)