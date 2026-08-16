### Q3. Write a Python program to find all the unique words and count the
### frequency of occurrence from a given list of strings. Use Python set data type.

def word_frequency(words) :
    unique_words = set(words)

    for word in unique_words :
        
        count = words.count(word)
        
        print(word, ":", count)


words = ["apple", "banana", "apple", "orange", "banana", "apple", "mango"]

print("Unique words and their frequency :")

word_frequency(words)