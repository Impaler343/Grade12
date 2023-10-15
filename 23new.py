'''
--Program 23--

Write a menu-driven program for inserting records into the MySQL table and handling appropriate queries using Python-MySQL Interface with the following menu: 

    Menu 
    1. Insert Records 
    2. Display Records 
    3. Department Wise 
    4. Gender Wise 
    5. Date Wise 
    6. Order by Salary / DateOfJoining / E_Name 
    7. Details of Max and Min Salary 
    8. Names starting with 
    9. Given department count 
    10. Exit
'''

import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = 'Crowbeard101!', database = 'people')
c = mydb.cursor(buffered = True)

def insert():
    x = []
    while True:
        t = ()
        e_no = int(input("Enter the Employee Number: "))
        e_name = input("Enter the Employee Name: ")
        dept = input("Enter the Department name: ")
        title = input("Enter the Job name: ")
        salary = int(input("Enter your salary: "))
        gen = input("Enter your gender: ")
        doj = input("Enter your Date of join(in date format): ")
        print()
        t = (e_no,e_name,dept,title,salary,gen,doj)
        x+=(t,)
        y = input("Enter 'y' to continue: ")
        if y != 'y':
            break
    for d in x:
        c.execute(f"insert into emp_details values{d}")
    mydb.commit()  

def display():
    c.execute("select * from emp_details")
    n = int(input("Enter the number of records to be displayed: "))  
    print()
    while True:
        x = c.fetchmany(n)
        if x:
            print(tabulate(x,headers=['E_No','E_Name','Dept','Title','Salary','Gender','DOJ'], tablefmt = "fancy_grid"),"\n")   
            en = input("Press enter to continue: ")
        else:
            break


def dep_count():
    print('''
    #1 To view records of a specific Dept 
    #2 To view records for all Depts ''')
    print()
    y = input("Enter your choice: ")
    if y == '1':
        w = input("Enter the department name: ")
        print()
        c.execute(f"select dept,count(*) from emp_details where dept = '{w}'")     
        x = c.fetchall()
        if x[0][0]:
            print(tabulate(x,headers=['Dept','Count'],tablefmt = "fancy_grid"),"\n")
        else:
            print("\nDepartment does not exist\n")    
    elif y == '2':
        c.execute("select dept, count(*) from emp_details group by dept")
        x = c.fetchall()
        print(tabulate(x, headers=[
              'Dept', 'Count'], tablefmt="fancy_grid"), "\n")

              
def gen():
    m = input("Enter the Gender to display:(M or F) ")
    print()
    c.execute(f"select * from emp_details where gender = '{m}'")
    x = c.fetchall()
    if x:
        print(tabulate(x, headers=[
              'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")
    else:
        print("\nInvalid Gender\n")    


def date():
    d = input("Enter the reference date(In YYYY-MM-DD): ")
    print()
    op = input("Enter 'B' for before or 'A' for after the given date: ")
    print()
    if op.lower() == 'b':
        c.execute(f"select * from emp_details where DOJ < '{d}'")
        x = c.fetchall()
        if x:
            print(tabulate(x, headers=[
                  'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")
        else:
            print("\nNo records\n")    
    elif op.lower() == 'a':
        c.execute(f"select * from emp_details where DOJ > '{d}'")
        x = c.fetchall()
        if x:
            print(tabulate(x, headers=[
                  'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")
        else:
            print("\nNo records\n")
def orderby():
    op = input("Enter the parameter to order by['e_name' or 'salary' or 'DOJ']: ")
    print()
    ord = input("Enter the mode of display['asc' or 'desc']: ")
    print()
    c.execute(f"select * from emp_details order by {op} {ord}")
    x = c.fetchall()
    print(tabulate(x, headers=[
          'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")

def max_min():
    print('''\n
    #1 To display maximum salary details
    #2 To display minimum salary details
    \n''')
    w = input("Enter your choice: ")
    print()
    if w == '1':
        c.execute("select * from emp_details where salary = (select max(salary) from emp_details)")
        x = c.fetchall()
        print(tabulate(x, headers=[
              'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")
    elif w == '2':
        c.execute("select * from emp_details where salary = (select min(salary) from emp_details)")
        x = c.fetchall()
        print(tabulate(x,headers=['E_No','E_Name','Dept','Title','Salary','Gender','DOJ'],tablefmt = "fancy_grid"),"\n")

def name_start():
    s = input("Enter the sub-string to check names: ")
    print()
    c.execute(f"select * from emp_details where e_name like '{s}%'")
    x = c.fetchall()
    print(tabulate(x, headers=[
          'E_No', 'E_Name', 'Dept', 'Title', 'Salary', 'Gender', 'DOJ'], tablefmt="fancy_grid"), "\n")

def rec_dept_count():
    n = int(input("Enter the reference Dept count: "))
    print()
    c.execute(f"select dept,count(dept) from emp_details group by dept having count(*) = {n}")
    x = c.fetchall()
    if x:
        print(tabulate(x, headers=[
              'Dept', 'Count'], tablefmt="fancy_grid"), "\n")
    else:
        print("\nNo records\n")
while True:
    print('''\n
    #1 Insert Records
    #2 Display Records
    #3 Department Count
    #4 Genderwise
    #5 Datewise
    #6 Order by salary/name/DOJ
    #7 Max and Min Salary
    #8 Names starting with __
    #9 Records with given Dept Count
    #10 Exit\n''')
    z = input("Enter your choice: ")
    print()
    if z == '1':
        insert()
    elif z == '2':
        display()
    elif z == '3':
        dep_count()
    elif z == '4':
        gen()
    elif z == '5':
        date()
    elif z == '6':
        orderby()
    elif z == '7':
        max_min()
    elif z == '8':
        name_start()
    elif z == '9':
        rec_dept_count()
    elif z == '10':
        print("Exiting now...")
        break
