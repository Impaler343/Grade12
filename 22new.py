'''
--Program 22--

Write a menu-driven program for table creation using Python - MySQL Interface with the following menu: 

    Menu 
    1. Create Database 
    2. Show Created Database and Tables 
    3. Add Attribute to Table 
    4. Modify Attribute 
    5. Drop Attribute 
    6. Exit
'''

import mysql.connector
from tabulate import tabulate
mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = 'Crowbeard101!')
c = mydb.cursor()
created = None
t_name = None

def d_create():
    global created,name,t_name
    created = True
    name = input("Enter the database name:")
    print()
    c.execute(f"create database if not exists {name}")
    c.execute(f"use {name}")
    t_name = input("Enter the table name:")
    c.execute(f"create table if not exists {t_name}(e_no int,e_name char(30),dept char(25),title char(25),salary int)")

def d_show():
    global created
    if created:
        print("\nThe created database is:",name,"\n")
        c.execute("show tables")
        x = c.fetchall()
        for i in x:
            c.execute(f"desc {i[0]}")
            x = c.fetchall()
            x = [i[:3] for i in x]
            print(tabulate(x,tablefmt = "fancy_grid"),"\n")

    else:
        print("\nCreate a database first")   

def addAttribute():
    col = input("Enter the column name: ")
    da = input("Enter the datatype: ")
    print()
    c.execute(f"alter table {t_name} add {col} {da}")        
    c.execute(f"desc {t_name}")
    x = c.fetchall()
    x = [i[:3] for i in x]
    print(tabulate(x,tablefmt = "fancy_grid"),"\n")

def modifyAttribute():
    col = input("Enter the column name: ")
    da = input("Enter the datatype: ")
    print()
    c.execute(f"alter table {t_name} modify {col} {da}")        
    c.execute(f"desc {t_name}")
    x = c.fetchall()
    x = [i[:3] for i in x]
    print(tabulate(x, tablefmt="fancy_grid"), "\n")
    
def deleteAttribute():
    col = input("Enter the column name: ")
    c.execute(f"alter table {t_name} drop {col}")        
    c.execute(f"desc {t_name}")
    x = c.fetchall()
    x = [i[:3] for i in x]
    print(tabulate(x, tablefmt="fancy_grid"), "\n")
    
while True:
    print('''
    #1 Create database
    #2 Show created database and table
    #3 Add Attribute to the table
    #4 Modify Attribute
    #5 Drop Attribute
    #6 Exit\n ''')
    z = input("Enter your choice:")
    print()
    if z == '1':
        d_create()
    elif z == '2':
        d_show()
    elif z == '3':
        addAttribute()
    elif z == '4':
        modifyAttribute()
    elif z == '5':
        deleteAttribute()    
    elif z == '6':
        print("Exiting now...")
        break

