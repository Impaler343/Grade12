
'''                                                                                  
from tabulate import tabulate
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = 'Crowbeard101!') #Database object created
print(mydb) #Object code displayed
print(mydb.is_connected()) #Will give True
mycurs = mydb.cursor() #Cursor object created
mycurs.execute("create database schoo") #Execute command is the same as giving commands in command line client
mycurs.execute("show databases")
for i in mycurs: HAVE to iterate to display
    print(i)
mycurs.execute("use schoo")
mycurs.execute("create table ma(ID int,NAME char(20))")
mycurs.execute("insert into ma(ID,name) values(99,'Mary')")
mycurs.execute("select * from ma")
for i in mycurs:
    print(i)
mycurs.execute("desc ma")
for i in mycurs:
    print(i)
'''

import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = "Crowbeard101!",database='people')#Notice how we connect to database directly(Optional)
c = mydb.cursor()

#A Database Connection Object controls the connection to the database and represents a unique session with a database connected from within a script 
#A Database Cursor is a special control structure that facilitates the row by row processing of records in the resultset
#A Result Set refers to a logical set of records that are refetched from the database by executing an SQL query and made available to the application program. Its use includes the extraction of data whenever needed

while True:
    no = int(input("Enter employee number:"))
    name = input("Enter the name:")
    dept = input("Enter the department:")
    gen = input("Enter the gender:")

    var = "insert into we values( {}, '{}', '{}', '{}' )".format(no,name,dept,gen) #{} are place holders. If its in quotes - char type
    c.execute(var)
    mydb.commit() #To reflect changes immediately(use for update delete and insert)
    z = input("Continue?(Enter 'y')")
    if z != 'y':
        break

t = input("enter the table name:")
c.execute("select * from {}".format(t))
for i in c:
    print(i)

n = int(input("Enter the number:"))
c.execute("select * from we where EmpNo = {}".format(n))
for i in c:
    print(i)

orderby = input("Enter the column:(name/department)")
how = input("Enter the order:(asc/desc)")
c.execute("select * from we order by {} {}".format(orderby,how))
for i in c:
    print(i)

gen = input("Enter the gender(m/f):")
c.execute("select gender,count(*) from we group by gender having gender = '{}'".format(gen))
for i in c:
    print(i)

dep = input("Enter the department:")
gen = input("Enter the gender:")
c.execute("select * from we where dept = '{}' and gender = '{}' ".format(dep,gen)) #OR c.execute("select * from we where dept = '{dept}' and gender = '{gend}' ".format(dept = dep,gend = gen))(Named arguments)
for i in c:
    print(i)

c.execute("select * from we") #CURSOR INSTANCE/RESULTANT SET
c.fetchall() #gets all the outputs from the cursor's resultant set above(use same logic for below)

c.execute("select * from we") #CURSOR INSTANCE/RESULTANT SET
a = c.fetchmany(2) #gets given number of records in table
print(c.rowcount) #gives 2
for b in a:
   print(b) #gives the first 2 records

a = c.fetchmany(2)
print(c.rowcount) #GIVES 4 NOT 2 hence gives the number of rows that have been retreived so far from the cursor
for b in a:
  print(b) #Will give next records
      #Keep track of the pointers

c.execute("update we set dept  = 'froth' where name = 'frog'")
      #UPDATE DOESNT HAPPEN UNLESS YOU DO commit() in mysql, auto commit happens
mydb.commit()
mydb.close() #To close the connection
