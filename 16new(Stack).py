'''
--Program 16--

Write a menu-driven program to perform stack operations on student details stack with the following menu: 

    Menu 
    1: Push 
    2: Pop 
    3: Peep 
    4: Exit
'''

stk = []
l = []

def display():
    if stk:
        print()
        print(stk[len(stk)-1],"  <--- TOP")
        for i in range(len(stk)-2,-1,-1):
            print(stk[i])
        print()
    else:
        print("Stack Empty")

def push(l,stk):
    while True:
        n = int(input("Enter the roll number: "))
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))
        l = [n,name,marks]
        stk.append(l)
        display()
        y = input("Enter 'y' to continue: ")
        print()
        if y != 'y':
            break

def pop(stk):
    if stk:
        stk.pop()
        display()
    else:
        print("Stack Underflow")    

def peek(stk):
    if stk:
        print(stk[len(stk)-1],"  <--- TOP")
    else:
        print("Stack Empty")

while True:
    print('''
    #1 Push
    #2 Pop
    #3 Peek
    #4 Exit
    \n''')
    z = input("Enter your choice: ")
    print()
    if z == '1':
        push(l,stk)
    elif z == '2':
        pop(stk)
    elif z == '3':
        peek(stk)
    elif z == '4':
        print("Exiting now...")
        break
