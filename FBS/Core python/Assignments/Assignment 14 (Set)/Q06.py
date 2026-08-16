### Q6. Write a Python program to find the two numbers whose product is
### maximum among all the pairs in a given list of numbers. Use the Python set.

def max_product(a):
    max_product = 0
    max_pair = set()

    for i in range(len(a)):
        
        for j in range(i + 1, len(a)):
            
            product = a[i] * a[j]

            if product > max_product :
                
                max_product = product
                
                max_pair = {a[i], a[j]}

    print("Pair:", max_pair)
    print("Maximum Product:", max_product)


a = [2, 5, 3, 9, 4]

max_product(a)