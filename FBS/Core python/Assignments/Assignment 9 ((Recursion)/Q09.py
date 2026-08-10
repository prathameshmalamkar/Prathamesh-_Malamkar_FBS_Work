#### Q9.Write a program to calculate the m to the power n using recursion.

## calculate a recursion function
def power (p, k):
    if k > 0:
        return p * power (p, k - 1)
    else:
        return 1
    
## input as a user
p = int(input("Enter p :"))    
k = int(input("Enter k :"))   

## function call
result = power (p, k)

## output
print (result)
