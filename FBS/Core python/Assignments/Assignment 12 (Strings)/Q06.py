### Q6. Python Program to Take in a String and Replace Every Blank Space with Hyphen ?

def replace_space(str):
    
    return str.replace(" ", "-")
    
p = input("Enter the string :")

res = replace_space(p)

print(f"After replacing string :", res)