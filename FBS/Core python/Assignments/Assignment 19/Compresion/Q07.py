### Q)7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.
# result = [num
#           for num in range(1, 1001)
#           for digit in range(2, 10)
#           if num % digit == 0]
# print(result)

result = {
    num
    for num in range(1, 1001)
    for digit in range(2, 10)
    if num % digit == 0
}

print(result)