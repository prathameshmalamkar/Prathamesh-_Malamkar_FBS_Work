### Q8.  W rite a program to find reverse of a numbers ?

## calculate the reverse number
def reverse_number(num):
    rev = 0
    
## use the while loop in reverse number 
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

## input as a user
i = int(input("Enter a  reverse number :"))

## faction call
result = reverse_number(i)

## output
print(result)