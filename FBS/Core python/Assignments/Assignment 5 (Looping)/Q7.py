#### Q7. Write a program to solve the following series :
#### a. 1! + 2! + 3! + 4! + .....n!
#### b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#### c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#### d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
#### e. x - x2/3 + x3/5 - x4/7 + .... to n term



## input as a user
n = int(input("Enter the number:"))

## a. 1! + 2! + 3! + 4! + ......n!

total = 0
fact = 1
for i in range (1, n+1):
    fact = fact * i
    total += fact
print(f"Sum of series a. until {n} is {total}")

## b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

## let initialize total to save sum of series
sum = 0
for num in range (1, n+1):
    s = (num**num)
    sum += s
print(f"Sum of series b. until {n} is {sum}")

## c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

## let initialize total to save sum of series
sum = 0 
term = 1
for i in range (1, n+1):
    sum += sum *(n**i)
    term + term*2
print(f"Sum of series c. until {n} is {sum}")

## d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

## lets take input as a d
d = int(input("Enter the number:"))

## let initialize total to save sum of series
sum = 0 
for i in range (1, 11 ):
    sum += (d** i)/i
print(f"Sum of series d. until number 10 is {sum}")

## e. x - x2/3 + x3/5 - x4/7 + .... to n terms.

## lets take input as a x
x = int(input("Enter the ending value:"))

## let initialize total to save sum of series
d = 1
sign = 1
sum = 0
for i in range (1, n+1):
    sum += sign* (x**i)/d
    d += 2
    sign *= -1
print(f"Sum of series e. until {n} is {sum}")
    


