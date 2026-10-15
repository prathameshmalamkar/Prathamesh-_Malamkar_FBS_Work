# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following exceptions:

# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.

# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.

# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.

# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.

def calculator():
    try:
        num1 = int(input("enter the num1:"))
        num2 = int(input("enter the num2:"))
        operator = input("enter the operator you want(+,-,*,/):")



        if operator not in['+','-','*','/']:
            raise Exception("Invallid operator")

        if operator =='+':
            res = num1 + num2
        elif operator =="-":
            res = num1 - num2
        elif operator == '*':
            res= num1 * num2
        elif operator =='/':
            res =num1 /num2

        print("Result =",res)
    except ValueError as v:
        print("please enter valid number ")

    except ZeroDivisionError as z:
        print("cannot divide by zero")

    except Exception as e:
        print(e)

calculator()
    
        