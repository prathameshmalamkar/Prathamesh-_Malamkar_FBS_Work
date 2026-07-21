#### Q9. Write a program to print all numbers in a range divisible by a given number ?

# input from user that divisible for given number
start = int(input("Enter your starting number:"))
end = int(input("Enter your ending number:"))
num = int(input("Enter divisor:"))

# starting and ending input given from user
for i in range(start,end + 1):
    
    if i % num == 0:
        print(i)