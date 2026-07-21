#### Q10. Write a program to check if given number is perfect number ?

## input as a user
num = int(input("Enter your number."))

## variable store to the sum of divisor
sum = 0

## find divisor of loop
for i in range (1,num):
    if num % i == 0:
        sum = sum + i
 
## Check the perfect number       
if sum == num:
   print(num,"The perfect number.")
else:
    print(num,"The not perfect number.")
