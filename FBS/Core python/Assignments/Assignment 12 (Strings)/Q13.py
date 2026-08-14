### Q13. Python Program to count number of digits and letters in a string.

def count_digits_letters(str):
    digits = 0
    letters = 0
    
    for i in str :
        if i >= '0' and i <= '9' :
            digits = digits + 1
        elif (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') :
            letters = letters + 1
                    
    return digits, letters

p = input("Enter a string :")


digits, letters = count_digits_letters(p)

print(f"Number of Digits :", digits)
print(f"Number of Letters :", letters)