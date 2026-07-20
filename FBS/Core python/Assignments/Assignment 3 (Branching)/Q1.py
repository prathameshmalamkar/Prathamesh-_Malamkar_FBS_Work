#### Q1. Write a program to check if the given number is positive or negative ?

## The program check a given number is positive or negative

# input from user
num=int(input("Enter a number."))

# check number is neutral
if(num == 0):
    print("The number is neutral.")
    
# Check number is positive
elif(num > 0):
    print("The number is positive.")
    
# check number is negative
else:
    print("The number is negative.")
