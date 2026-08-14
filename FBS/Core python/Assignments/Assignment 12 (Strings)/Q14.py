### Q14. Python Program to count the occurrences of ach word in a string.

def count_words(str):
    words = str.split()
    result = {}

    for i in  words :
        if i in result :
            result[i] = result[i] + 1
        else:
            result[i] = 1

    return result


q = input("Enter a string: ")

res = count_words(q)

print(f"The Word occurrences:", res)