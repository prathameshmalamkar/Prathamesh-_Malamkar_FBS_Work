### Q2. Write a program to check if given number is Armstrong or not using recursive function ?

## calculate the recursive function
def armstrong (n, digits):
    if n == 0 :
        return 0 
    digit = n % 10
    return (digit ** digits) + armstrong (n // 10, digits)

## input as a user
num = int(input("Enter a number n :"))
digits = len(str(num))

## function call
result = armstrong (num, digits)

## output:
if result == num :
    print(f"{num},It is a Armstrong number !")

else:
    print(f"{num},It is not Arstrong number !")
    



