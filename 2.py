'''
--Program 2--

Write a menu-driven program in python with the following menu: 

    Menu 
    1. List generation 
    2. Guess Number 
    3. Shuffle and Predict 
    4. Exit 
    
Import random and time modules and use appropriate functions wherever required.

'''

import random as R
import time
l = []
def create_list():
    global l
    start = int(input("Enter the start number: "))
    end = int(input("Enter the stop number: "))
    lenn = int(input("Enter the length of the list: "))
    l = []
    for _ in range(lenn):
        l.append(R.randint(start,end))
    print('\n',l)    

def guess():
    x = R.choice(l)
    print('''\nThe Computer has made its choice
       You have 3 turns\n''')
    chances = 3
    while chances:
        g = int(input("Enter your guess: "))
        if g == x:
            print("\nYou guessed the right number!\n")
            break
        else:
            print("\nWrong!!\n")
            chances -=1
    else:
        print("\nYour 3 chances are over. You lost :(")        

def shuffle():
    print('''\nYou will be shown the list twice
You will have to guess all the elements of the list''')
    print('\n',l,'\n')
    time.sleep(2)
    print('\n'*30)
    R.shuffle(l)
    print('\n',l,'\n')
    time.sleep(2)
    print('\n'*30)
    newl = [int(i) for i in input("Enter the elements of the list seperated by spaces: ").split()]
    d1 = {i:l.count(i) for i in l}
    d2 = {i:newl.count(i) for i in newl}
    if d1 == d2:
        print("You guessed the right list! ")
    else:
        print("You guessed it wrong :(\n")
        print(f"The original list: {l}\n")
        print(f"Your guess: {newl}")

while True:
    print('''\n  Menu
#1 List Generation
#2 Guess Number
#3 Shuffle and Predict
#4 Exit\n''')

    z = input("Enter your choice: ")
    print()
    if z == '1':
        create_list()
    elif z == '2':
        guess()    
    elif z == '3':
        shuffle()
    elif z == '4':
        print("Exiting now...")
        break
