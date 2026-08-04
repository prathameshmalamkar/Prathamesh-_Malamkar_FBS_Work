### Q3. Write a program to reverse a given number using recursive function ?

## calculate recursive function
def reverse (num):
    
    if num > 0:
        digit = num % 10
        
        print (digit, end = "")
        reverse (num // 10)
        
## input as a user
p = int(input("Enter a number :"))

## function call
reverse(p)
    