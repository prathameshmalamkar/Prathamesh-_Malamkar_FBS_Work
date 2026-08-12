a = 'aba'
b = ' '

for i in range (len(a) - 1, 0 - 1, - 1):
    b += a [i]

if a == b :
    print("String is palindrome.")
else :
    print("String is not palindrome.")