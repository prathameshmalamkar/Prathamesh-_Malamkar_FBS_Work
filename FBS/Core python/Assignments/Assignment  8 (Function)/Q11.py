### Q11. Write a program  to check if a given number is Armstrong number or not. For each task create separate functions ?

## Function to count digits:
def count_digits(num):
    count = 0
    temp = num
    
## use the while loop in function separate 
    while temp > 0:
        count = count + 1
        temp = temp // 10
    return count

## check the Armstrong number
def armstrong(num):
    digits = count_digits(num)
    temp = num
    total = 0

## use the while loop in armstrong number
    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10

## use the if else method :
    if total  == num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

# Input as a user 
n = int(input("Enter a number: "))

# Function call
armstrong(n)