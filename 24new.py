'''
--Program 24--

Write a menu-driven program for updating records in the MySQL table using Python-MySQL Interface with the following menu: 

    Menu 
    1. Update EName/Dept/Title/Gender 
    2. Update Specific Record Salary 
    3. Mass Salary Update 
    4. Exit
'''

import mysql.connector
from tabulate import tabulate
mydb = mysql.connector.connect(host = 'localhost',user = 'root',db = 'people',password = 'Crowbeard101!')
c = mydb.cursor(buffered = True)

def update_details():
    n = int(input("Enter employee number: "))
    print()
    s = input("Enter field to update('e_name'or 'dept' or'title' or 'gender'): ")
    print()
    new = input("Enter the new value for chosen column: ")
    print()
    c.execute(f"update emp_details set {s} = '{new}' where e_no = {n}")
    c.execute("select * from emp_details")   
    mydb.commit() 
    x = c.fetchall()
    print(tabulate(x, headers=[
          'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")

def update_sal():
    n = int(input("Enter employee number: "))
    print()
    sal = int(input("Enter the new salary: "))
    print()
    c.execute(f"update emp_details set salary = {sal} where e_no = {n}")
    c.execute("select * from emp_details")   
    mydb.commit() 
    x = c.fetchall()
    print(tabulate(x, headers=[
          'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")

def mass_update_sal():
    sal = int(input("Enter the salary hike: "))
    print()
    c.execute(f"update emp_details set salary = salary+{sal}")
    c.execute("select * from emp_details")
    mydb.commit() 
    x = c.fetchall()
    print(tabulate(x, headers=[
          'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")
    
while True:
    print('''\n
    #1 Update Name/Dept/Job/Gender
    #2 Update specific record - Salary
    #3 Mass salary update
    #4 Exit\n''')
    z = input("Enter your choice: ")
    print()
    if z == '1':
        update_details()
    elif z == '2':
        update_sal()
    elif z == '3':
        mass_update_sal()
    elif z == '4':
        print("Exiting now...")
        break
