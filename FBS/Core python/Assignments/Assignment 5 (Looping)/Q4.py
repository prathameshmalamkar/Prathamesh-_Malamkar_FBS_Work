#### Q4. Write a program to print armstrong number within a given range ?

## input as a user start and end 
start = int(input("Enter your starting number:"))
end = int(input("Enter your ending number:"))

for num in range (start, end + 1):
    temp = num
    d = len(str(num))
    total = 0
    
    
    while(temp > 0):
        digit = temp % 10
        total = total + (digit ** d)
        temp = temp // 10
        
    if total == num:
        print(num)
        
    