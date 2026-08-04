### Q1. Write a program to find sum of following series using recursive functions:
###   i. 1! + 2! + 3! + 4! +..... + n!
### Note : For fact and sum two recursive functions

## find the recursive function of fact
def fact(n):
    if n == 1:
        return 1
    return n * fact (n - 1)

## calculate recursive function to find sum of fact series
def sum_fact(n):
    if n == 1:
        return fact (1)
    return fact (n) + sum_fact (n - 1)

## input as a user
a = int(input("Enter a number n :"))

## function call
res = sum_fact (a)

## output
print(res)