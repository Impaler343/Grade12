'''
--Program 3--

Write a menu-driven program in python to create a text file with the following menu: 

    Menu 
    1. Create File 
    2. Count 'my' 
    3. Count 3 letter words 
    4. Count letters 'e' and 'u' 
    5. Exit
 
'''

def create_file():
    with open('3.txt', 'w+') as file:
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

def mycount():
    with open ('3.txt','r') as file:
        count = 0
        for c in file.read().split():
            if c.lower() == 'my':
                count +=1
    if count:
        print("Count of 'my' :", count)
    else:
        print("No 'my' found")                

def count3():
    with open ('3.txt','r') as file:
        count = 0
        for c in file.read().split():
            if len(c) == 3:
                count +=1
    if count:
        print("Number of 3-letter words: ", count)
    else:
        print("No 3-letter words found")   

def counteu():
    with open ('3.txt','r') as file:
        counte = countu =  0
        for c in file.read():
            if c.lower() == 'e':
                counte +=1
            elif c.lower() == 'u':
                countu +=1    
    print("Number of 'e's: ", counte,'\n')
    print("Number of 'u's: ", countu,'\n')



while True:
    print('''\n  Menu
    #1 Input
    #2 Count of 'my'
    #3 Count 3 letter words
    #4 Count letters 'e' and 'u'
    #5 Exit
    \n''' )
    z = input("Enter your choice: ")
    print()
    if z == '1':
        create_file()
    elif z == '2':
        mycount()
    elif z == '3':
        count3()
    elif z == '4':
        counteu()    
    elif z == '5':
        print("Exiting now...")
        break
