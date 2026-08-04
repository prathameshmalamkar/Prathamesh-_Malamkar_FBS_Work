### Q7. Write a program to find sum of digits using recursion ? 

## calculate a recursion function of sum of digit
def sum_digit (n):
    if n == 0 :
        return 0
    else:
        return (n % 10 ) + sum_digit (n // 10 )
    
## input as a user 
num = int(input("Enter a sum of digit :"))

## function call
result = sum_digit(num)

## output
print(result)
    