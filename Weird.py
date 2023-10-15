
import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',passwd='Crowbeard101!',user = 'root',database = 'MockPr')

c = mydb.cursor(buffered = True)

p = input("Enter the platform: ")
c.execute("select * from movie_details where platform = '{p}'")
print(c.fetchall())

c.execute("select title from movie_details order by title desc")
print(c.fetchall())

c.execute("select max(rating) from movie_details")
print(c.fetchall())
