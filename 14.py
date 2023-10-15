'''
--Program 14--

Write a menu-driven program to create a CSV file with student details having the following menu: 
    
    Menu 
    1: Insertion 
    2: Search 
    3: Deletion 
    4: Update 
    5: Exit
'''

import csv
from tabulate import tabulate

def insert():
    with open('14.csv','w',newline = '') as file:
        a = csv.writer(file)
        a.writerow(['Roll No.','Name','Marks'])
        while True:
            l = []
            l.append(int(input("Enter your Roll No.: ")))
            l.append(input("Enter your name: "))
            l.append(int(input("Enter your marks: ")))
            a.writerow(l)
            print()
            z = input("Enter 'y' to continue:")
            print()
            if z != 'y':
                break

def search():
    n = int(input("Enter the Roll No."))
    print()
    with open('14.csv','r') as file:
        a = csv.reader(file)
        next(a)
        for c in a:
            if int(c[0]) == n:
                print(tabulate([c], headers=['Roll No','Name','Marks'], tablefmt='fancy_grid'))
                return
        else:
            print("Not found")


def display():
    print()
    with open('14.csv','r') as file:
        file.seek(0)
        a = csv.reader(file)
        print(tabulate(a, tablefmt='fancy_grid'))  


def update():
    global d
    r = input("Enter the Roll No.: ")
    with open('14.csv', 'r', newline='') as file:
        d = False
        a = csv.reader(file)
        ml = [['Roll No.', 'Name', 'Marks']]
        next(a)
        for c in a:
            if c:
                if c[0] == r:
                    x = input(
                        "Enter 1 to update Roll No. OR 2 to update Name OR 3 to update Marks: ")
                    if x == '1':
                        n = int(input("Enter the new Roll No.: "))
                        ml.append([n, c[1], c[2]])
                    elif x == '2':
                        n = input("Enter the new Name: ")
                        ml.append([c[0], n, c[2]])
                    elif x == '3':
                        n = int(input("Enter the new Marks:"))
                        ml.append([c[0], c[1], n])
                    d = True
                else:
                    ml.append(c)
    with open('14.csv', 'w', newline='') as file:
        if d:
            file.seek(0)
            x = csv.writer(file)
            x.writerows(ml)

def delete():
    global d
    d = False
    r = int(input("Enter the Roll No.: "))
    print()
    with open('14.csv','r',newline = '') as file:
        a = csv.reader(file)
        next(a)
        ml = [i for i in a if int(i[0]) != r]
        file.seek(0)
        nl = [i for i in a]
        if nl != ml:
            d = True
    with open('14.csv','w',newline = '') as file:
        if d:
            ml.insert(0,['Roll No.','Name','Marks'])
            x = csv.writer(file)
            x.writerows(ml)      

while True:
    print('''\n    Menu
#1 Insert
#2 Search
#3 Update
#4 Deletion
#5 Exit \n''')
    z = input("Enter your choice:")
    print()
    if z == '1':
        insert()
        display()
    elif z == '2':
        search()
    elif z == '3':
        update()
        if d:
            display() 
        else:
            print("\nNot Found\n")
    elif z == '4':
        delete()
        if d:
            display()
        else:
            print("\nNot Found\n") 
    elif z == '5':
        print("Exiting now...")
        break
