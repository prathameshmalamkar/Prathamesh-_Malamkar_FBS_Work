### Q3. Python Program to Detect if Two Strings are Anagrams ?

def check_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if check_anagram(s1, s2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")