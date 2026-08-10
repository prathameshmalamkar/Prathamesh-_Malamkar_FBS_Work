### Q4. Sum of all odd numbers between 1 to n ?

## calculate all odd number 1 to n
def sum_odd(n):
    total = 0
    
## use the for loop in odd number 1 to n 
    for i in range(1, n+1):
        if i % 2 !=0:
            total = total + i
    return total

## input as a user
p = int(input("Enter a number :"))

## faction call
result = sum_odd(p)

## output
print(result)
    
