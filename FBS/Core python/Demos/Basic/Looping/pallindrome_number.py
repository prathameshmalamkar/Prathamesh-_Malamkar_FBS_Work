num = int(input("Enter number:"))

temp = num
rev = 0
while(num > 0):
    d= num % 10
    num = num // 10 
    rev = rev * 10 + d
    
if (temp == rev):
    print("Pallindrome number.")
else:
    print("Not a pallidrome number.")