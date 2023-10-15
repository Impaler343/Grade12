'''
--Program 12--

Write a menu-driven program in python to create a binary file with the following menu. (Use dictionaries and file pointer) 

    Menu 
    1. Insertion 
    2. Deletion 
    3. Search 
    4. Update 
    5. Exit
'''

import pickle

def insert():
    with open('9b.dat','wb') as file:
        d = {}
        while True:
            d['name'] = input("Enter the name:")
            d['class'] = int(input("Enter the class:"))
            d['age'] = int(input("Enter the age:"))
            print()
            pickle.dump(d,file)
            z = input("Enter 'y' to continue:")
            print()
            if z != 'y':
                break

def display():
    with open('9b.dat','rb') as file:
        try:
            while True:
                print(pickle.load(file))
        except EOFError:
            pass

def search():
    n = input("Enter the name to search:")
    print()
    with open('9b.dat','rb') as file:
        try:
            c = True
            while True:
                a = pickle.load(file)
                if a['name'] == n:
                    print(a)
                    c = False
                    return
        except EOFError:
            if c:
                print("Not found")

def update():
    with open('9b.dat','rb+') as file:
        try:
            c = True
            while True:
                t = file.tell()
                a = pickle.load(file)
                if a['class'] == 12 and a['age'] != 18:
                    a['age'] = 18
                    file.seek(t,0)
                    pickle.dump(a,file)
                    c = False
        except:
            if c:
                print("No changes made")
            else:
                display()

def delete():
    with open('9b.dat','rb+') as file:
        n = input("Enter the name to delete: ")
        print()
        l = []
        try:
            c = True
            while True:
                a = pickle.load(file)
                if a['name'] != n:
                    l.append(a)
                else:
                    c = False
        except EOFError:
            if c:
                print("Not found")
            else:
                for c in l:
                    print(c)
while True:
    print('''\n    Menu
#1 Insert
#2 Search
#3 Updation
#4 Deletion
#5 Exit\n ''')
    z = input("Enter your choice:")
    print()
    if z == '1':
        insert()
        print()
        display()
    elif z == '2':
        search()
    elif z == '3':
        update()
    elif z == '4':
        delete()
    elif z == '5':
        print("Exiting now...")
        break
