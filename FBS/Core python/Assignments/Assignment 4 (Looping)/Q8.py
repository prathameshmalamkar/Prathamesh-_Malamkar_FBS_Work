#### Q8.Write a program to find which numbers are divisible by 7 and multiple of 5 in a given range ?

# the input for start and end the range
start = int(input("Enter your starting number:"))
end = int(input("Enter your ending number:"))

# loop for given range
for i in range(start, end + 1):
    
## check the number division by 7 and mult of 5
    if i%7==0 and i%5==0:
        print(i)