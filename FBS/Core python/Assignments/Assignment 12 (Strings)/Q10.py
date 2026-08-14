### Q10.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.

def larger_string(str1, str2):
    count1 = 0
    count2 = 0
    
    for i in str1 :
        count1 = count1 + 1
        
    for j in str2 :
        count2 = count2 + 1
        
    if count1 > count2 :
        return str1
    elif count2 > count1 :
        return str2
    else :
        return "Both string are equal."
    
c = input("Enter a first string :")
d = input("Enter a second string :")

# str1,str2 = larger_string(c,d)

print(f"larger string :", (larger_string(c,d)))
        