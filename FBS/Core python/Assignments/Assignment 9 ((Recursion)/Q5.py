### Q5. Write a program to find factorial using recursion ?

## calculate a recursive function of factorial
def fact (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact (n - 1)
    
## input as a user
num = int(input("Enter a number :"))

## faction call
result = fact(num)

## output
print(result)