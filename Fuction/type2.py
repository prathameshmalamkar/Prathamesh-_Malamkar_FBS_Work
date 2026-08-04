# With passing parameter (with input)
# Without returning value (without output)

def addition(num1, num2):          #Formal parameters / arguments
    
    sum = num1 + num2
    
    print(f"Addition of {num1} and {num2} is {sum}.")
    


n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
    
addition(n1, n2)                  #Actual parameters / argumets