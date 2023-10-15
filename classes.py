from tkinter import *

'''
class Employee:
    def __init__(self,e_no,e_name,salary): #need not be in same order as assignment
        #Giving values by constructor
        self.e_no = e_no
        self.e_name = e_name
        self.salary = salary

    def display(self):
        print(self.e_no,self.e_name,self.salary)


#Creating objects
#Constructor gets activated when we create objects
emp1 = Employee(100,"A",5000)
emp2 = Employee(10,"B",500)

Employee.display(emp1) #need to pass object name
emp1.display() #another way to do the same

# type(3) will give class int
# type(emp1) will give class main.Employee

#Giving values one by one
emp1.e_no = 100
emp1.e_name = "A"
emp1.salary = 5000

emp2.e_no = 10
emp2.e_name = "B"
emp2.salary = 500
'''
class Win1:
    def __init__(self,master):
        self.master = master
        self.master.title("Login window")
        self.master.geometry("400x400+0+0")
        self.button = Button(self.master,text = "fde",command = lambda : self.new_window(2,Win2)).pack()

    def new_window(self,number,Win2):
        self.new = Toplevel(self.master)
        Win2(self.new,master)

class Win2:
    def __init__(self,master,num):
            self.master = master
            self.master.title("Login window")
            self.master.geometry("400x400+0+0")
            self.quit  = Button(self.master,text = f"Quit window{num}",command = self.close_window)
            self.quit.pack()

    def  close_window(self):
        self.master.destroy()

root = Tk()
wind_1 = Win1(root)
root.mainloop()
