
# def Login():
#     # print("time started")
#     # print("logger added")
#     # print("Before login")
#     print("login is done")
#     # print("timer stopped")
#     # print("logger removed")
#     # print("After login")

# Login()


# def Logout():
#     # print("time started")
#     # print("logger added")
#     # print("Before login")
#     print(type(Logout))
#     # print("timer stopped")
#     # print("logger removed")
#     # print("After login")

# Logout()

# def AdminLogin():
#     # print("time started")
#     # print("logger added")
#     # print("Before login")
#     print("Adminlogin is done")
#     # print("timer stopped")
#     # print("logger removed")
#     # print("After login")

# AdminLogin()





# we can store function in variable
# def Demo():
#     print("I am in Demo")

# x = Demo
# print(type(Demo))
# print(type(x))
# x() # print data in demo


# passed the function as an argument to another function
# def fun1():
#     print("I am from fun1")

# def demoFun(a):
#     print("i am from demofunction")
#     a()

# demoFun(fun1)

# return inner function from outer function
# def Outer():
#     print("Outer fun is called")
#     def innerfun():
#         print("Inner fun is called")
#     return innerfun()

# a=Outer()
# a


# clouser
# def Outer():
#     print("Outer fun is called")
#     var ="Virat"
#     def innerfun():
#         print("Inner fun is called",var)
#     return innerfun()

# a=Outer()
# a

def demo(fun):
    print("Decorator is called")
    def Wrapper():
        print("before calling")
        fun()
        print("after calling")
    return Wrapper

@demo
def login():
    print("\n login \n")


@demo
def logout():
    print("\n logout \n")

login()
logout()