### Q1. Write a program to calculate area of rectangle ?

## Calculate area of rectangle
def area_rectangle(length,width):
    area = length*width
    return area

## input as a user
a = int(input("Enter your length:"))
b = int(input("Enter your width:"))
    
## function call
result = area_rectangle(a, b)

## output
print(result)

