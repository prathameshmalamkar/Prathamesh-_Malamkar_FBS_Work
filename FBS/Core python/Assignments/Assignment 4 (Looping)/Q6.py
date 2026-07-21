#### Q6. Write a program check if a given number is prime number or not ?

## the input from user
num = int(input("Enter your number:"))

## check the number is grater than 1    
if(num > 1):
    for i in range(2, num ):
        print(i)
        if(num % i == 0):
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")    
else:
    print(f"{num} is not a prime number.")