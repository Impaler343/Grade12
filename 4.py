'''
--Program 4--

Write a menu-driven program in python to create a text file with the following menu: 

    Menu 
    1. Create file 
    2. Find longest line 
    3. Count & display line starting with specified letter 
    4. Reverse all words starting with 'i' 
    5. Exit

'''

def create_file():
    with open('4.txt', 'w+') as file:
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

def longest():
    with open('4.txt', 'r') as file:
        x = file.readlines()
        l = [len(i) for i in x]
        print('\n',x[l.index(max(l))])

def count_line():
    with open('4.txt', 'r') as file:
        d = False
        chr = input("Enter the letter: ")
        count = 0
        for c in file.readlines():
            if c[0] == chr:
                d = True
                print('\n',c)
                count += 1
        if d:        
            print(f"\nCount: {count}")
        else:
            print("No lines")            

def revI():
    with open('4.txt', 'r') as file:
        sen = ''
        var = file.readline()
        while var:
            d = var.strip('\n').split()
            for c in d:
                if c.lower().startswith('i'):
                    sen = sen + ' ' + c[::-1]
                else:
                    sen = sen + ' ' + c
            sen = sen + '\n'
            var = file.readline()

        print(sen)


while True:
    print('''\n  Menu
    #1 Input
    #2 Find longest line
    #3 Count and display lines starting with specified letter
    #4 Reverse all words starting with 'i'
    #5 Exit
    \n''')
    z = input("Enter your choice: ")
    print()
    if z == '1':
        create_file()
    elif z == '2':
        longest()
    elif z == '3':
        count_line()
    elif z == '4':
        revI()
    elif z == '5':
        print("Exiting now...")
        break
