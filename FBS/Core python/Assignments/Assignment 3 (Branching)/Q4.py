# Program to check whether a triangle is valid or not using sides

# Input the three sides from the user
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))


if (side1+side2>side3) and (side2+side3>side1) and (side1+side2>side2):
    print("Triangle is Valid")
else:
    print("Triangle is Not Valid")