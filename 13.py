'''
--Program 13--

Write a python program to create and read a CSV file with book details using ‘\t’ as a delimiter.
'''

import csv
from tabulate import tabulate

with open('13.csv','w+',newline = '') as file:
    ml = []
    while True:
        l = []
        l.append(int(input("Enter the serial no.: ")))
        l.append(input("Enter the book name: "))
        l.append(input("Enter the author name: "))
        ml.append(l)
        print()
        z = input("Enter 'y' to continue: ")
        print()
        if z != 'y':
            break

    x = csv.writer(file,delimiter = '\t')
    x.writerows(ml)

    file.seek(0)
    y = csv.reader(file,delimiter = '\t')
    ul = list(y)
    print(tabulate(ul, headers=["S No.",
          "Book", "Author"], tablefmt='fancy_grid'))
