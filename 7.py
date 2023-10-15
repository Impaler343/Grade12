'''
--Program 7--

Write a menu-driven program in python to create a text file with the following menu: 

    Menu 
    1. Create File 
    2. Separate words by … 
    3. Exit
'''

def create_file():
    with open('7.txt', 'w+') as file:
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

def chr_sep():  
    chr = input("Enter the character: ")  
    print()
    with open('7.txt', 'r') as file:
        x = file.readlines()
        l = [i.replace(' ',chr) for i in x]
        for c in l:
            print(c)


while True:
    print('''\n     Menu
    #1 Input
    #2 Words seperated by _
    #3 Exit
    \n''')
    z = input("Enter your choice: ")
    print()
    if z == '1':
        create_file()
    elif z == '2':
        chr_sep()
    elif z == '3':
        print("Exiting now...")
        break