
def num():
    yield 1
    yield 2
    yield 3
    yield 4
g= num()
print(next(g))
print(next(g))

# generator using for loop
def demo():
    for i in range(100,201):
        yield i
g =demo()
print(g) # it gives object so for value we use next keyword
print(next(g)) 
print("next value...")
print(next(g))
print("next value...")
print(next(g))
print("next value...")
print(next(g))