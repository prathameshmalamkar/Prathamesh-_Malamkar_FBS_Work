### Q7.  W rite a program to find Sum of digit of a numbers ?

## calculate the sum of digit
def sum_digit(num):
    total = 0
    
## use the while loop in sum of digit
    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10
    return total

## input as a user
h = int(input("Enter a number :"))

## faction call
result = sum_digit(h)

## output
print(result)