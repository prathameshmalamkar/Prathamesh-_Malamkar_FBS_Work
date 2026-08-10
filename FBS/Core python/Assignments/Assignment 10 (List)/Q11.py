### Q11. Write a program to print all numbers which are divisible by m and n in the list ?

def divisible(li, m, n):
    
    new = []

    for val in li :
        if val % m == 0 and val % n == 0 :
            new += [val]
            
    print(new)
    
li = [10, 12, 15, 30, 40, 60]

m = 3
n = 2

divisible = divisible(li, m, n)
        

        
