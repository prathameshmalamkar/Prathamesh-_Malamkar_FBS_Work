### Q9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String.

def count_string(str):
    words = 0
    characters = 0
    
    for ch in str :
        if ch == " " :
            words =  words + 1
        else :
            characters = characters + 1
            
    words += 1
    # characters += 1
    
    return  words, characters

d = input("Enter a string :")

words,character = count_string(d)

print(f"The number of words :", words)
print(f"The number of characters :", character)
            
    