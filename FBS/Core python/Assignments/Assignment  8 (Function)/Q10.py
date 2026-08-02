### Q9. Write a program to check if entered year is leap or not ?

## check the leap year :
def leap_year(year):
    
## use the if else method:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("The leap year :")
    else:
        print("The not a leap year :")
        
## input as a user
year = int(input("Enter a  leap year :"))

## faction call
leap_year(year)