Q = []
l = []

def display():
    if Q:
        print("\nF --> ",end = '')
        for c in Q:
            print(c,end = ' <-- ')
        print("R\n")
    else:
        print("Queue Empty")

def enQueue(l,Q):
    while True:
        n = int(input("Enter the roll number: "))
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))
        l = [n,name,marks]
        Q.append(l)
        display()
        y = input("Enter 'y' to continue: ")
        print()
        if y != 'y':
            break

def deQueue(Q):
    if Q:
        Q.pop(0)
        display()
    else:
        print("Queue Empty")    

def peek(Q):
    if Q:
        print(Q[0],"  <--- FRONT")
    else:
        print("Queue Empty")

while True:
    print('''
    #1 enQueue
    #2 deQueue
    #3 Peek
    #4 Exit
    \n''')
    z = input("Enter your choice: ")
    print()
    if z == '1':
        enQueue(l,Q)
    elif z == '2':
        deQueue(Q)
    elif z == '3':
        peek(Q)
    elif z == '4':
        print("Exiting now...")
        break
