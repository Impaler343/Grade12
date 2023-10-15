'''
--Program 11--

Write a menu-driven program in python to create a binary file with the following menu:

    Menu 
    1. Insertion 
    2. Deletion 
    3. Search 
    4. Update 
    5. Exit 
    
Open the binary file in the correct mode wherever required and perform updation using a temporary file.(os module)
'''

import pickle,os
from tabulate import tabulate

def insert(l):
    with open('11.dat','ab') as file:
        pickle.dump(l,file)

def display():
    with open('11.dat','rb') as file:
        ml = []
        try:
            while True:
                a = pickle.load(file)
                ml.append(a)
        except EOFError:
                pass
    print(tabulate(ml,headers = ["Roll No.","Name","Marks"], tablefmt='fancy_grid'))

def search(r):
    with open('11.dat','rb') as file:
        try:
            n = False
            while True:
                a = pickle.load(file)
                if a[0] == r:
                    print(tabulate([a], headers=["Roll No.", "Name", "Marks"], tablefmt='fancy_grid'))
                    return
                else:
                    n = True
        except EOFError:
            if n:
                print("Not found")


def update():
    with open('temp.dat','wb') as temp:
        with open('11.dat','rb') as file:
            try:
                while True:
                    a = pickle.load(file)
                    if a[2] < 35:
                        a[2] += 5
                    pickle.dump(a,temp)
            except EOFError:
                pass

    os.remove('11.dat')
    os.rename('temp.dat','11.dat')

def delete(r):
    with open('temp.dat','wb') as temp:
        with open('11.dat','rb') as file:
            try:
                n = True
                while True:
                    a = pickle.load(file)
                    if a[0] != r:
                        pickle.dump(a,temp)
                        n = False
            except EOFError:
                if n:
                    print("Not found")
    os.remove('11.dat')
    os.rename('temp.dat','11.dat')

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
        while True:
            r = int(input("Enter the roll no.:"))
            n = input("Enter the name:")
            m = int(input("Enter the marks:"))
            print()
            l = [r,n,m]
            insert(l)
            y = input("Enter 'y' to continue: ")
            print()
            if y != 'y':
                break
        print()    
        display()
    elif z == '2':
        r = int(input("Enter the Roll No. to be read:"))
        print()
        search(r)
    elif z == '3':
        update()
        display()
    elif z == '4':
        r = int(input("Enter the Roll No. to delete:"))
        print()
        delete(r)
        display()
    elif z == '5':
        print("Exiting now...")
        break
