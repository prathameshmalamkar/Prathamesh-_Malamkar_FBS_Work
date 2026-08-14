### Q8. Python Program to Remove the Characters of Odd Index Values in a String

def remove_odd_index(str):
    result = " "
    
    for i in range (len(str)):
        if i % 2 == 0 :
            result += str[i]
            
    return result

b = input("Enter string :")

res = remove_odd_index(b)

print(f"After removing character of odd index value :", res)
            