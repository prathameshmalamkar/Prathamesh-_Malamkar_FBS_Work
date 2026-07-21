#### Q3. Write a program to print fibonacci series upto n ?

## input from user to fibonacci series upto n

n = int(input("How many fibonacci numbers you want:"))

## initialize first and second number
a = -1
b = 1

## the print fabonacci series
for i in range(n):
    c = a+b
    print(c)
    
    a = b
    b = c