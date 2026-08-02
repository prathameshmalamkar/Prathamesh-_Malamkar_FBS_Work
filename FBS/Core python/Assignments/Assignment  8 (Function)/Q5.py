### Q5. Sum of all prime numbers between 1 to n ?

## calculate the number
def is_prime(num):
    if num < 2:
        return False
    
## use the for loop 
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

## calculate the sum of prime number 1 to n
def sum_prime(n):
    total = 0
    
## use the for loop of sum of prime number
    for i in range(2, n + 1):
        if is_prime(i):
            total = total + i   
    return total

## input as a user
q = int(input("Enter a number :"))

## faction call
result = sum_prime(q)

## output
print(result)
    