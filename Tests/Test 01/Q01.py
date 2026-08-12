### Q1. Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user):


def area_perimeter(l, b, r):
    area = (l * b) + (3.14 * r * r ) / 2
    perimeter = l + l + b + ( 3.14 * r ) 
    
    print("Area =", area)
    print("Perimeter =", perimeter)
    
length = int(input("Enter your length :"))
breadth = int(input("Enter your breadth :"))
radius = int(input("Enter your radius :"))

area_perimeter(length, breadth, radius)

