'''
--Program 8--

Write a menu-driven program in Python to create a text file and segregate all 3 letter words into a file and the remaining words into another using relative and absolute paths(os module) 
    Menu 
    1. Create File 
    2. Segregate words 
    3. Exit
'''

import os
path = ''

def inp():
    global path
    d = os.getcwd()
    print(f"Current Directory: {d}\n")
    f = input("Enter the file name to create: ")
    print()
    path = f"{d}\\{f}.txt"
    print(f"{path}\n")

    with open(path,'w+') as file:
        while True:
            s = input("Enter line: ")
            file.write(f"{s}\n")
            print()
            y = input("Enter 'y' to continue: ")
            print()
            if y != 'y':
                break
        file.seek(0)    
        print(file.read())


def segregate():
    global path
    d = os.getcwd()
    print(f"Current Directory: {d}\n")
    try:
        os.mkdir('NEW')
    except:
        pass    
    os.chdir('NEW')
    dn = os.getcwd()
    print(f"New Directory: {dn}\n")
    f = input("Enter the file name: ") + '.txt'
    print()
    new_path = f"{dn}\\{f}"
    print(f"{new_path}\n")

    with open(path,'r') as file1:
        with open(new_path,'w+') as file2:
            with open(r"C:\Users\raghu\OneDrive\Desktop\Programs\G12\8.txt", 'w+') as file3:
                for c in file1.read().split():
                    if len(c) == 3:
                        file2.write(c+' ')
                    else:
                        file3.write(c+' ')  
                file2.seek(0)
                file3.seek(0)            
                print("File in current directory: \n",file2.read(),'\n')
                print("File in 'NEW' directory: \n",file3.read(),'\n')




while True:
    print('''\n     Menu
    #1 Input
    #2 Segregate
    #3 Exit
    \n''')
    z = input("Enter your choice: ")
    print()
    if z == '1':
        inp()
    elif z == '2':
        segregate()
    elif z == '3':
        print("Exiting now...")
        break
