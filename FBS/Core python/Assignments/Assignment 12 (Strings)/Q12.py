### Q12. Python Program to count number of lowercase characters in a string.

def count_lowercase(str):
    count = 0
    
    for i in str :
        if i >= 'a' and i <= 'z' :
            count = count + 1
            
    return count

p = input("Enter a string :")

res = count_lowercase(p)

print(f"Number of lowercase character :", res)