### Q04. Remove all of the vowels in a string (take input from user)


str =input("enter a string:")
vowels=[ch for ch in str if ch not in "aeiou"]
print("".join(vowels))
