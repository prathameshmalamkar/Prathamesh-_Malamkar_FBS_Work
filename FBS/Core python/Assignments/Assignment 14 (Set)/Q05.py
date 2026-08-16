### Q5. Write a Python program to find the longest common prefix of all strings. Use the Python set.

def longest_common_prefix(words):
    prefix = ""

    for i in range (len(min(words, key=len))):
        
        chars = set(word[i] for word in words)

        if len(chars) == 1:
            
            prefix = prefix + words[0][i]
            
        else:
            break

    return prefix


words = ["flower", "flow", "flight", "flow"]

res = longest_common_prefix (words)

print(f"Longest Common Prefix:", res)