#A function is a subprogram that acts on data and often returns a value
#USEFULNESS
#To break code into smaller parts
#To reduce lines by calling functions

#Program execution begins with the first statement of the __main__ segment
#Built in Functions - Predefined functions that are always available for use(len,type,int,input)
#Module functions - Predefined in particular modules and can be used if the modules are imported(math,statistics)
#User Defined Functions - Defined by the programmer
#Parameters/Formal parameters/Formal arguments - Values received in the function definition/function header
#Arguments/Actual parameters/Actual arguments - The values being passed through the function call statement 
#When the function call statement must match the number and order of arguments as defined, in the function header, it is called positional argument matching
#A parameter having a default value in the function header is called default parameter
#Keyword arguments are the named arguments with assigned values being passed in the function call statement
#A function may return multiple values that may be received as a tuple or as individual variables
#Functions that return value are called fruitful or non-void functions
#Functions that dont return a value are called non-fruitful or void functions
#The program parts in which a particular variable, piece of code or data value is legal and can be accessed is called Variable Scope
#LEGB Rule (Local,Enclosing,Global,Builtin) means a local variable having the same name as a global variable, hides the global variable in its function
#The global statement cannot be undone in a code block, once declared global, it cant be reverted back to local
#A namespace is a named logical environment holding groups of related objects; its member object is referred without any prefix
#A namespace is a collection of names that uniquely identifies an object. Implemented with the help of dictionaries(WOW, thats why the recently defined function is executed remember?)
#The system stores names and local variables of a function in the area of memory called stack
#When a program execution starts, a global namespace is created and after execution it is removed, same for a function call and its local arguments
#The time for which a variable or name remains in memory is called its Lifetime
#Heap memory is the one used during runtime
#When dynamic typing happens, if a particular object is not used for a long time, the garbage collector empties it

#Docstring - Tripled quoted multiline comments usually used to describe a function or a module

#In pass by reference, the variable is passed into the function directly. The variable acts a Package that comes with it’s contents(the objects). 
#Any operation performed by the function on the variable or the object will be directly reflected to the function caller.(MUTABLE TYPES, lists and all)
#The function receives the reference of the same object in the memory as referred by the caller.

#In pass by value the function is provided with a copy of the argument object passed to it by the caller. That means the original object stays intact. 
#All changes made are to a copy of the same and stored at different memory locations.(IMMUTABLE TYPES, strings int and all)
#The function creates an entirely new variable for itself.

#RULES for parameters and calling :- sample header -- def interest(prin,cc,rate = 0.9,time=2)
#Positional arguments be followed by default and keyword arguments eg: interest(rate=0.8,5000,3) is wrong
#You cannot give multiple values to an argument while calling it eg: interest(5000,prin = 800,cc=4) is wrong (prin assigned twice)
#All positional arguments must be assigned values in the call eg: interest(500) is wrong (cc is missing)
#If all are keyword arguments, they can be in any order

#Function Body - The indented statements
#Indentation - The blank space at the beginning of a block
#print(__name__) will give __main__, else if the script is running another imported module, the __name__ will have __thenameofthemodule__

#know the difference between return and print and both at the same time and their order

# def yay():
#     print('oppg')
#     #return 'popg' #OR no return statement
# print(yay()) #OR just yay()

# def f(a,b):
#     global x,y #NO error, a global is created
#     x = a+b
#     a,y=a+x,a*x
#     print(a,b,x,y)
# f(5,10)
# print(f(b=x,a=y))

# def check(a):
#     for i in range(len(a)):
#         a[i] = a[i] + 5
#     a = a + [10]
#     return a
# b = [1,2,3,4]
# c = check(b)
# print(c,b) # [6,7,8,9,10] [6,7,8,9]

'''
--Program 1--

Write a menu-driven program in python using functions with the following menu: 

    Menu 
    1. Positional and Default Arguments 
    2. Keyword Arguments 
    3. Variable Length Arguments 
    4. Variable Length Keyword Arguments 
    5. Multiple Return Value 
    6. Exit

'''

from tabulate import tabulate

def interest(p,n=2,r=0.09):
    return(f"Interest: {p*n*r}")

def total_sum(a,*arg): #Takes a sequence 
    s=0
    for i in arg:
        s +=i
    print('\n',a,s,'\n')

def stu_info(stud,**kwarg): #Takes a dictionary, have to pass keyword arguments
    print(stud,'\n')
    print(tabulate(kwarg.items(), tablefmt='fancy_grid'))

def sum_avg(*arg):
    s1=0
    for i in arg:
        s1 +=i
        avg=s1/6
    return(s1,avg)

while True:
    print('''\n    Menu
#1 Positional and Default Arguments
#2 Keyword Arguments
#3 Variable length Arguments
#4 Variable length keyword Arguments
#5 Multiple Return values
#6 Exit\n    ''')
    z = int(input("Enter your choice:"))
    print()
    if z == 1:
        p = int(input("Enter principle: "))
        print()
        t = int(input("Enter time: "))
        print()
        print(interest(p,t))                        
    elif z == 2:
        p = int(input("Enter principle: "))
        print()
        r = int(input("Enter rate: "))
        print()
        print(interest(p,r)) 

    elif z == 3:
        total_sum("Sum is",1,2,3)
        total_sum("Sum is",1,2,3,4,5)

    elif z == 4:
        stu_info("Student information",Roll_number=1,name="John",grade=12,marks=100)

    elif z == 5:
        a,b = sum_avg(1,2,3,4,5,6)
        c = sum_avg(1,2,3,4,5,6)
        print(f"Sum: {a} Average: {b}")

    elif  z == 6:
        print("Exiting now...")
        break                  
