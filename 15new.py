'''
--Program 15--

Write a menu-driven program to create a CSV file with Employee details having the following menu: 

    Menu 
    1: Insertion 
    2: Display specific column 
    3: Exit
'''

import csv
from tabulate import tabulate

def create_file():
    with open('15.csv', 'w+', newline='') as file:
        ml = [['Emp_No','Emp_Name','Dept']]
        while True:
            l = []
            l.append(int(input("Enter the Employee No.: ")))
            l.append(input("Enter the Employee name: "))
            l.append(input("Enter the Department: "))
            print()
            ml.append(l)
            y = input("Enter 'y' to continue: ")
            if y != 'y':
                break
        x = csv.writer(file)
        x.writerows(ml)

def rec_count():
    cols = input("Enter columns to display seperated by space: ").split()
    with open ('15.csv','r') as file:
        x = csv.reader(file)
        ul = list(x)
    
    d={}
    for c in range(3):
        if ul[0][c] in cols:
            d[ul[0][c]] = [i[c] for i in ul]
    ml = []
    for k in range(len(ul)):
        l=[]
        for e in d.values():
            l.append(e[k])
        ml.append(l)    

    print()
    print(tabulate(ml,tablefmt='fancy_grid'))

    d = x.line_num
    print("\nNo. of records iterated: ",d-1)
    
        

while True:
    print('''\n   Menu
#1 Input
#2 Display Specific Column
#3 Exit\n''')

    z = input("Enter your choice: ")
    print()
    if z == '1':
        create_file()
    elif z == '2':
        rec_count()
    elif z == '3':
        print("Exiting now...")
        break

    
