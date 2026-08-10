### Q6. Write a program to print Fibonacci series using recursion ?

## calculate recursive function of fibonacci series
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)
    
## input as a user       
num = int(input("Enter a number of terms :"))

## using for loop in fibonacci series
def fibonacci_series (n):
    for i in range (n):
        print (fibonacci(i))

## function call
fibonacci_series(num)

      
    
