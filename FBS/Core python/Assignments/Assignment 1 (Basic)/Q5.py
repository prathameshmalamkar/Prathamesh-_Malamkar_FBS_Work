### Q.5 Write a program to enter P,T,R and calculate Compound Interest

##  The perform of P,T,R to  calculate of Compound Interest

## Take input in principal amount
P=int(input("Enter your principal amount:"))

## Take input in time in years
T=int(input("Enter your time in years:"))

## Take input in rate of interest
R=int(input("Enter your rate of interest:"))

## calculate amount using of Compound Interest formula
A=P*(1+R/100)**T

## calculate Compound Interest formula
CI=A-P

## Diplay result
print(A,2)
print(CI)

