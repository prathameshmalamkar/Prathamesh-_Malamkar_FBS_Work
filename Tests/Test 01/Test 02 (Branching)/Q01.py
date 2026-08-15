### Q1. Write a program to accept year from user and check if it is a leap year or not. 

year = int(input("Enter a Year :"))

if year % 400 == 0 :
    print("The Leap Year :")
    
elif year % 4 == 0 and year % 100 != 0 :
    print("The Leap Year :")
    
else :
    print("The Not a Leap Year :")