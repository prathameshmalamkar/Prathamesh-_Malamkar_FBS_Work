#### Q1. Write a program to print all odd numbers until n ?

## input from user all odd numbers until n
n= int(input("Enter the value of n:"))

## the odd number print
for i in range(1,n+1):
    if i % 2 != 0:
        print(i)