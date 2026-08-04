def chkPallindrome():
    num = int(input("Enter number:"))
    temp = num
    rev = 0
    
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d
        
    if(num == rev):
        print("The number is pallindrome.")
    else:
        print("The number is not pallindrome.")
        
chkPallindrome()