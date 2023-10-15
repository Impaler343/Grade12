'''
--Program 25--

Write a menu-driven program for deleting records from the MySQL table using Python-MySQL Interface with the following menu: 

    Menu 
    1. Delete Specific Record 
    2. Delete Records between Given Dates 
    3. Exit
'''

import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(user = 'root',host = 'localhost',db = 'people',password = 'Crowbeard101!')
c = mydb.cursor(buffered = True)

def del_spec():
    n = int(input("Enter the employee number: "))
    print()
    c.execute(f"delete from emp_details where e_no = {n}")
    c.execute("select * from emp_details")
    x = c.fetchall()
    print(tabulate(x, headers=[
          'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")
    mydb.commit()

def del_date():
    d1 = input("Enter the starting date(In YYYY-MM-DD): ")
    print()
    d2 = input("Enter the ending date(In YYYY-MM-DD): ")
    print()
    c.execute(f"delete from emp_details where DOJ between '{d1}' and '{d2}'")
    c.execute("select * from emp_details")
    x = c.fetchall()
    print(tabulate(x, headers=[
          'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")
    mydb.commit()

while True:
    print('''\n
    #1 Delete specific record
    #2 Delete records for given date range
    #3 Exit
    \n''')
    z = input("Enter your choice: ")
    print()
    if z == '1':
        del_spec()
    elif z == '2':
        del_date()
    elif z == '3':
        print("Exiting now...")
        break        
