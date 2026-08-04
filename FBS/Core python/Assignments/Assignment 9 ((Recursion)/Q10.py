#### Q10.Write a program to reverse a number using recursion.

## calculate a recursion function of reverse number
def rev (num, sum = 0):
    if num == 0:
        return sum
    
    digit = num % 10
    sum = sum * 10 + digit
    
    return rev (num // 10, sum)

## input as a user 
num = int(input("Enter number:"))

## function call
d = rev (num)

## output
print (d)