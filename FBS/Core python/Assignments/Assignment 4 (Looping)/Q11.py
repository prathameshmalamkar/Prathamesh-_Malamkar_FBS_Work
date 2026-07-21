#### Q11. Write a program to check if given number strong number ?

## input as a user
num = int(input("Enter your number."))

## store the original number
temp = num 

## variable to store sum of factorial
sum = 0

## while loop use
while (temp > 0):
    digit = temp % 10
    
## find the factorial 
    fact = 1
    for i in range (1, digit + 1):
        fact = fact * i
    
## the factorial sum 
    sum = sum + fact
    
## remove the last digit
    temp = temp // 10
  
## check the strong number and not   
if sum == num:
    print(num,"The strong number.")
else:
    print(num,"The not strong number.")
