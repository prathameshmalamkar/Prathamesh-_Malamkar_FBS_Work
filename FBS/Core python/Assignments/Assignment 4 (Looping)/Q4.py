#### Q3. Write a program to print factorial of a number  ?

## input from user of factorial number

n = int(input("Enter your number:"))

## initialize factorial number
fact = 1

## the calculate  factorial number using loop
for i in range(1, n+1):
    fact = fact * i
    
## display result
print("Factorial", fact)