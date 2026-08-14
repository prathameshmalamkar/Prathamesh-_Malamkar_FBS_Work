### Q5.Python Program to Count the Number of Vowels in a String

def vowel_count(str):
    count = 0
    
    for char in str :
        if char in "a,e,i,o,u,A,E,I,O,U":
            count += 1

    return count

b = input("Enter the string :")

res = vowel_count(b)

print("Number of vowel :", res)