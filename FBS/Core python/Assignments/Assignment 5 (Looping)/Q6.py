#### Q1. Write a program to print first n prime numbers  ?

## input as a user 
n = int(input("Enter how many prime number:"))

## lets program
for num in range (n + 1):
    if (num > 1):
        for i in range (2, num // 2 + 1):
             if num % i == 0:
                break
        else:
            print(num)
    else:
        print(f'{num} is not prime number not composite!')