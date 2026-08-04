#### Q4.Write a program to find sum of n numbers using recursion ?

## calculate recursive function of sum of n number
def sum_of_series (n):
    if n > 0 :
        return n + sum_of_series (n - 1)
    else:
        return 0
    
## input as a user
n=int(input("Enter a sum of n number :"))

## function call
res=sum_of_series(n)

## output
print(res)    
    

