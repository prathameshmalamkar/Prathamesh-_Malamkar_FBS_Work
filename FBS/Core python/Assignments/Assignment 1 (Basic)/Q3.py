#### Q3. Program to find quotient and remainder of two numbers ?

# To find quotient and remainder of two numbers a & b

a=int(input("enter your first number:"))
b=int(input("enter your second number:"))

# as we know for normal division use "/" in python and it gives us quotient and to get remainder we have "%" also k/a modulas division

quotient=a/b
remainder=a%b

# lets display result

print(f"the quotient and remainder of {a} and {b} are quotient:{quotient},remainder:{remainder}")