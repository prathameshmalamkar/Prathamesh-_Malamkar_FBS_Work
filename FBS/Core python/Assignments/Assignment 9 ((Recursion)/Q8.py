### Q8. Write a program to check whether a number is prime or not using recursion ?

## calculate a recursion function
def prime (num, n):
    if num <= 1 :
        return False
    elif n == 1 :
        return True
    elif num % n == 0 :
        return False
        return prime (num , n - 1)
 
 ## prime or not in recursion function
def is_prime (num):
    if prime  (num, num // 2):
        print (f"{num}, It is a prime number :")
        
    else :
        print(f"{num}, It is not prime number :")
    
 ## input as a user
num = int(input("Enter a number :"))   

## function call
is_prime (num)