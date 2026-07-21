#### Q3. Write a program to print sum of series upto n ?

## input from user to sum of series upto n

n = int(input("Enter your number:"))

## initialize sum variable
sum = 0

## the loop for sum of series 1 to n
for i in range(1, n+1):
    sum = sum + i
    
## display result
print("Sum of series", sum)