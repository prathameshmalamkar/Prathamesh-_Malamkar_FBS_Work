### Q6. Write a program to find print the following Fibonacci series using function :
### 1 1 2 3 5 8 n terms

## calculate the fibonacci series
def fibonacci(n):
    a = 1
    b = 1
    
## use the for loop in fibonacci series
    for i in range(n):
        print(a, end = " ")
        c = a + b 
        a = b
        b = c
        
## input as a user
w = int(input("Enter number of term :"))

## function call
result = fibonacci(w)

## output
print(result)
