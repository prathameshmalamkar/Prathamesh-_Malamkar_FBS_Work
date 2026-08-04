# Without passing parameter (without input)
# With returning value (without output)

def addition():
    
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))
    
    sum = num1 + num2
    
    return sum

res = addition()

print(res)