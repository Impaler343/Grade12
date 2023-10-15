'''
--Program 5--

Write a menu-driven program in python to create a text file with the following menu: 

    Menu 
    1. Create file 
    2. Most Frequent Word with its frequency 
    3. Frequency of all words
    4. Exit
'''

from tabulate import tabulate

def create_file():
    with open('5.txt', 'w+') as file:
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


def most_f():
    global d
    m = max(d.values())
    for c in d:
        if d[c] == m:
            k = c
    print(f"Most Frequent word: {k}\nFrequency: {m}")

def freq():
    global d
    l = []
    for c in d:
        l.append([c,d[c]])
    print(tabulate(l, headers=['Word', 'Frequency'], tablefmt='fancy_grid'))             

while True:
    print('''\n     Menu
    #1 Create file
    #2 Most Frequent Word with its frequency 
    #3 Frequency of all words
    #4 Exit
    \n''')
    with open('5.txt', 'r') as file:
        x = file.read().split()
        d = {i: x.count(i) for i in x}

    z = input("Enter your choice: ")
    print()
    if z == '1':
        create_file()
    elif z == '2':
        most_f()
    elif z == '3':
        freq()
    elif z == '4':    
        print("Exiting now...")
        break
