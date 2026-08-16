### Q9. Write a Python program to find all the unique combinations of 3 numbers
###     from a given list of numbers, adding up to a target number.

def find_combinations(numbers, target) :
    result = []

    for i in range(len(numbers)) :
        
        for j in range(i + 1, len(numbers)) :
            
            for k in range(j + 1, len(numbers)) :

                if numbers[i] + numbers[j] + numbers[k] == target :
                    
                    result.append((numbers[i], numbers[j], numbers[k]))

    return result


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tar = 10

res = find_combinations (num, tar)

print(res)