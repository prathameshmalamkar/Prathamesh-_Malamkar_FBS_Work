#### Q1. Write a program to print all even numbers until n ?

## input from user all even numbers until n
n= int(input("Enter the value of n:"))

## the even number print
for i in range(0,n+1):
    if i % 2 == 0:
        print(i)