### Q3. Python Program to Check if a Given Key Exists in a Dictionary or Not.

def check_key(dict,key):
    if key in dict:
        print("The key is Exists :")
    else :
        print("The key is not Exists :")
        
dict1 = {'a': 10, 'b': 20, 'c': 30, 'd':40}

a = input("Enter a key :")

res = check_key(dict1, a)
