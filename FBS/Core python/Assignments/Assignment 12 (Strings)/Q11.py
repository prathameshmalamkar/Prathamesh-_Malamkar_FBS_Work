### Q11. Python Program to replace every blank space with hyphen in a string.

def replace_space(str):
    result = ""
    
    for i in str :
        if i == " " :
            result = result + "-" 
        else :
            result = result + i
            
    return result

a = input("Enter a string :")

res = replace_space(a)

print(f"After replacing space :", res)
                            
            