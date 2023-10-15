'''
--Program 10--

Write a menu-driven program in python to create binary file with the following menu: 

    Menu 
    1. Insertion 
    2. Deletion 
    3. Search 
    4. Update 
    5. Exit 
    
Open the binary file in the correct mode wherever required and perform updation without using a temporary file.
'''

import pickle
from tabulate import tabulate

def insert():
    with open('10.dat','wb') as file:
        ml = []
        while True:
            l = []
            l.append(input("Enter the name: "))
            l.append(int(input("Enter the Roll No.: ")))
            l.append(int(input("Enter the marks: ")))
            print()
            ml.append(l)
            z = input("Enter 'y' to continue:")
            print()
            if z != 'y':
                break
        pickle.dump(ml,file)

def display():
    with open('10.dat','rb') as file:
        while True:
            try:
                a = pickle.load(file)
            except:
                break
    print(tabulate(a,headers = ['Name','Roll No','Marks'],tablefmt = 'fancy_grid'))
    print("\n")

def search():
    r = int(input("Enter the Roll No.: "))
    print()
    with open('10.dat','rb') as file:
        a = pickle.load(file)
        for c in a:
            if c[1] == r:
                print(tabulate([c], headers=['Name', 'Roll No', 'Marks'],tablefmt='fancy_grid'))
                break
        else:
            print("Not found")

def update():
    r = int(input("Enter the Roll No.: "))
    print()
    with open('10.dat','rb+') as file:
        d = False
        a = pickle.load(file)
        for c in a:
            if c[1] == r:
                x = input("Enter 1 to update Name OR 2 to update Roll No. OR 3 to update Marks: ")
                print()
                if x == '1':
                    n = input("Enter the new Name: ")
                    print()
                    c[0] = n
                elif x == '2':
                    n = int(input("Enter the new Roll No.: "))
                    print()
                    c[1] = n
                elif x == '3':
                    n = int(input("Enter the new Marks:"))
                    print()
                    c[2] = n
                d = True
        if d:
            file.seek(0)
            pickle.dump(a,file)
        else:
            print("Not found")

def delete():
    r = int(input("Enter the Roll No.: "))
    with open('10.dat','rb+') as file:
        new = []
        a = pickle.load(file)
        for c in a:
            if c[1] != r:
                new.append(c)
        if not new:
            print("Not found")
        else:
            file.seek(0)
            pickle.dump(new,file)

while True:
    print('''\n    Menu
#1 Insert
#2 Search
#3 Updation
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
        display()
    elif z == '4':
        delete()
        display()
    elif z == '5':
        print("Exiting now...")
        break
