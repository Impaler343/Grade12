#A library refers to a collection of modules that together cater to specific type of needs or applications
#Python standard library has math, cmath, random, statistics, Urlibb
#cmath module - for manipulation of complex numbers
#Urllib module - Provides URL handling functions to access websites in the program
#NumPy - Provides advance math stuff and tools to manipulate arrays
#SciPy - Provides algorithmic and mathematical tools for scientific calculations
#tkinter - Provides tools to integrate GUIs
#Matplotlib - Provides tools to produce charts, graphs and plots
#Site Packages folder has all the default libraries and packages that can be imported and is the target directory in which all installed Python packages are placed, by default
#The sys.path attribute gives important information about PYTHONPATH which specifies the directories that the python interpreter will look in, when importing modules
#the first value of sys.path is ' ', which means it will look in the current directory first before looking into site packages

#Act of partitioning a program into individual components is called modularity
#Advantages of Modules
#Reduces complexity to some degree
#Creates a number of well defined, documented boundaries within the program

#A python module is a file(.py file) containing variables, classes, definitions, statements and functions related to a particular task whose functionality can be reused at will
#A python file saved with .py extension is saved in 'script' mode(not run mode or interactive mode)
#A package is a collection of modules
#  DOUBLE DOT ..\phase2\results.dat             phase2 is the main folder, we are in one of the subfolders, and results.dat is in that phase2 folder
# ..\First Term\Result1.xlxs           Admin is the main folder and we are in 'Final' folder, and result1 is in first term folder which is in admin folder

#3 ways to import - import,from import, import *
'''
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace) 
print(string.punctuation)
print(string.capwords('i ama boy')) Does the same stuff as 'title'

abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
0123456789abcdefABCDEF
\t\n\r\x0b\x0c
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''

'''
import my_module as mm

print("Main Program")

mm.welcome()
#AMAZING!!
'''

'''
def display():
    print("In built function")

from my_module import display

print(display()) # The IMPORTED one will be used according to LEGB rule
'''
'''
from my_module import display

def display():
    print("In built function")

print(display()) # The INBUILT one will be used according to LEGB rule

'''
'''
from mod1 import change
from mod2 import change
change(5) Prints the mod2's result as it was imported last
'''
'''
import math
help(math) #All the functions and everything else in the module(basically docstring)

dir(math) #All the names in the defined in the module

help(mm)# The docstrings that WE wrote are displayed('This is my module' and all)
'''

'''
from math import pow as ll # DONT give module name with the function that you are importing(import math.pow)
from math import * #Imports everything
print(ll(2,3))
'''

'''
import my_module #Seperate namespace is created in the main program, from which you can pick up different stuff
from my_module import welcome #Firstly, DONT put brackets at the end while importing a function
                              #Secondly, a seperate namespace WILL NOT be created, and the thing will come into the main programs namespace(name clashes possible)
'''

'''
#If you import modules twice or thrice, there wont be errors.

#STEPS TO CREATE A MODULE:
#1 Make a folder
#2 Create a blank __init__.py file (to tell everyone that it is a library)
#3 Put your files in there

#ACCESSING FILES
#1 import __libraryname__.__filename__ as _name_
   OR
   from __libraryname__ import __filename__ as _name_
'''

#from Geometry import Rectangle as R, Circle as  C
# while True:
#     print('''\n    Menu
# #1 Area of circle
# #2 Area of rectangle
# #3 Perimeter of circle
# #4 Perimeter of rectangle
# #5 Exit \n''')
#     z = input("\nEnter your choice: ")
#     if z == '1':
#         r = float(input("Enter radius of circle:  "))
#         print("\nArea: ",C.c_area(r))
#     elif z == '2':
#         l = float(input("Enter length of rectangle: "))
#         b = float(input("Enter length of breadth: "))
#         print("\nArea: ",R.r_area(l, b,))
#     elif z == '3':
#         r = float(input("Enter radius of circle:  "))
#         print("\nPerimeter: ",C.per(r))
#     elif z == '4':
#         l = float(input("Enter length of rectangle: "))
#         b = float(input("Enter length of breadth: "))
#         print("\nPerimeter: ",R.per(l, b,))
#     elif z == '5':
#         print("Exiting now....")
#         break
