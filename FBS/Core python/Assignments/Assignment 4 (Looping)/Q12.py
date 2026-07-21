#### Q12. 12. Write a program to check if given number is Armstrong number or not ?
#### (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

## input as a user
num = int(input("Enter your number:"))

## store the original number
temp = num

count = len(str(num))

total = 0

## use the while loop
while(num > 0):
    d = num % 10
    total = total + (d ** count)
    num = num // 10
    print(total)
    
## check the armstrong number
if total == temp :
    print(num,"The number is armstrong.")
else:
    print(num, "The number is not armstrong.")

    