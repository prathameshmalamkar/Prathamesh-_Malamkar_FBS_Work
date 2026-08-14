### Q7. Python Program to Calculate the Length of a String Without Using a Library Function ?

def string_length(str):
    count = 0
    
    for ch in str :
        count += 1
    return count

a = input("Enter a string :")

res = string_length(a)

print(f"Length of string :", res)