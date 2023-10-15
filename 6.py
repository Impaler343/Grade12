'''
--Program 6--

Write a menu-driven program in python to create a text file with the following menu: 
    Menu 
    1. Create File 
    2. Capitalize Lines 
    3. Exit 
    
Open the file in the correct mode and capitalize each sentence in each line.
'''


def create_file():
    with open('6.txt', 'w+') as file:
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

def cap():
    with open('6.txt','r+') as file:
        for c in file.readlines():
            x = c.split('.')
            l = [i.capitalize() for i in x]
            m = '.'.join(l)
            print(m)

while True:
    print('''\n Menu
    #1 Input
    #2 Capitalize Lines
    #3 Exit
    \n''')
    z = input("Enter your choice: ")
    print()
    if z == '1':
        create_file()
    elif z == '2':
        cap()
    elif z == '3':
        print("Exiting now...")
        break
