### Q3. Write a program to find sum of following series using functions :
### a. 1+ 2 + 3 + 4+..... + n
### b. 1!+ 2! + 3! + 4!+..... + n!
### c. 1^1 + 2^2 + 3^3+ ...... n^n

## a. 1+ 2 + 3 + 4+..... + n

## calculate the sum of series from number 1 to n
def sum_series(n):
    total = 0
    
    ## use the for loop from 1 to n
    for i in range(1 , n + 1):
        total += i
    return total
    
## input as a user 
d = int(input("Enter your number n :"))

## function call
result = sum_series(d)

# ## output 
print(result)


## b. 1!+ 2! + 3! + 4!+..... + n!

## calculate the  factorial of  number 1! to n!
def factorial(num):
    fact = 1
    
## use the for loop of factorial
    for i in range(1, num + 1):
        fact = fact * (i)
    return fact

## calculate the sum of factorial series
def sum_factorial(n):
    total = 0
    
## use the for loop of sum of factorial 
    for i in range(1, n+1):
        total = total + factorial(i)
    return total

## input as a user
f = int(input("Enter your number d :"))

## faction call
result = sum_factorial(f)
    
## output 
print(result)


##c. 1^1 + 2^2 + 3^3+ ...... n^n
    
## calculate the sum of series from 1^1 to n^n
def sum_series(n):
    total = 0
    
### use the for loop from 1^1 to n^n number
    for i in range(1, n+1):
        total = total + (i ** i)
    return total 

## input as a user 
g = int(input("Enter your number p :"))

## faction call
result = sum_series(g)

## output
print(result)
