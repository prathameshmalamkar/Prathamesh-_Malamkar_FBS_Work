### Q8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.

def words_frequency(str):
    dict = {}
    
    words = str.split()
    
    for ch in words :
        if ch in dict :
            dict[ch] = dict[ch] + 1
        else :
            dict[ch] = 1
            
    return dict

a = input("Enter a String :")

res = words_frequency(a)

print(f"The Words Frequency :", res)