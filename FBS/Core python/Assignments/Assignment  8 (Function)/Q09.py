### Q9. Write a program to check if entered number is a palindrome or not ?

## check the palindrome number:
def palindrome(num):
    temp = num
    rev = 0
    
## use the while loop in palindrome number
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
        
    if temp == rev:
        print("The palindrome number :")
    else:
        print("The not a palindrome number :")
        
## input as a user
n = int(input("Enter a  reverse number :"))

## faction call
palindrome(n)
