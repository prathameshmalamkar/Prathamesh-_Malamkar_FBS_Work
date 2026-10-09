### Q02. Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.


def is_palindrome():
    num=11
    while True:
        rev=0
        original =num
        while(num >0):
            digit =num%10
            rev = rev *10 +digit
            num = num//10

        if(original ==rev):
            yield original
        num = original +1

        
g =is_palindrome()
print(next(g))
print(next(g))
print(next(g))
print(next(g))