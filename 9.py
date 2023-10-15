'''
--Program 9--

Write a menu-driven program in python to create a text file with the following menu: 

    Menu 
    1. Create File 
    2. Toggle case 
    3. Exit 
    
Toggle case and update the file
'''

def create_file():
    with open('9.txt', 'w+') as file:
        while True:
            s = input("Enter a sentence: ")
            print()
            file.write(s+'\n')
            y = input("Enter 'y' to continue: ")
            print()
            if y != 'y':
                break
        file.seek(0)
        print(file.read())

def swap():
    with open('9.txt','r+') as file:
        x = [i.swapcase() for i in file.readlines()]
        for c in x:
            print(c.strip('\n'))
        file.seek(0)    
        file.writelines(x)    

while True:
    print('''\n     Menu
    #1 Input
    #2 Toggle Case
    #3 Exit
    \n''')
    z = input("Enter your choice: ")
    print()
    if z == '1':
        create_file()
    elif z == '2':
        swap()
    elif z == '3':
        print("Exiting now...")
        break
