#Decorators are higher-order functions that take a callable (function, method, class) as an argument and return another callable.

# @decorator
# def decorated_func():
#     # Function body...
#     pass

#decorated_func = decorator(decorated_func) #This is what happened in the previous code

def add_messages(func):
    def _add_messages():
        print("This is my first decorator")
        func()
        print("Bye!")
    return _add_messages

@add_messages
def greet():
    print("Hello, World!")


























#INNER/NESTED FUNCTIONS
def fun1(m=8,n=10):
    global x
    x = 4
    y = 6
    print(m+n-x)
    def fun2():
        x = 5
        return x
    print(fun2())
a,b = 5,10
x = 20
fun1(b)
print(x)

def out(x,y):#Here x and y are local variables for out()
    def ins():
        print(x)#Here x is a nonlocal variable for ins()
    ins()
    def get_x():
        return x
    def get_y():
        return y
    def set_x(value):
        nonlocal x
        x = value
    def set_y(value):
        nonlocal y
        y = value
    def point():
        print(f"Point: {x},{y}")
    #Attaching getters and setters
    point.x_val = get_x
    point.y_val = get_y
    point.change_x = set_x
    point.change_y = set_y
out('HOUSE')
point = out(1,2)
point.get_x()
point.get_y()
point.set_x()
point.set_y()
#ins() This call gives an error as ins() is totally hidden from the global scope (ENCAPSULATION)

