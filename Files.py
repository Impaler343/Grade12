#Delimited text files are files in which a character is used to seperate each value. When its tab seperated it is txt, when it is comma seperated, it is csv
#Need for a file - To store information in the secondary storage device.
#A file is a collection of bytes stored in computer's secondary memory.
#Extension is the unique identity for a file.
#File object is also called file handle. It is a reference to a file on the disk.
#The file is automatically closed if the file handle is referenced to some other object!!
#file.close() make changes permanent(implicitly flushes) and disconnects OR file.flush() to make changes permanent NOW(forces the writing of data on disc still pending in output buffer)
#file = open('maa.txt','w') [Here pointer is placed at the first, so if there is something in the file before, it will be erased]
#file = open('maa.txt','r') [Here pointer is placed at first, BUT it will give FileNotFoundError if file doesnt exist]
#file = open('maa.txt','a') [Here pointer is placed at END, if there is already some info. If file is not there, it will create]
#file = open('maa.txt') [If mode is not there, DEFAULT is READ mode]
#file = open('maa.TXT','r') #WORKS !
#import os
#os.remove("goat.txt") #deletes this file
#os.rename("file2.txt","goat.txt") # renames file2 to goat
#file.seek(__offset__,__from_what) Offset - Number of bytes to read. from_what - pointer position. No Arguments raises an error
#0 - Go to starting of file
#1 - Go to file pointer
#2 - Got to file end
#You can move the file-pointer in the forward direction as well as the backward direction eg: file.seek(30,0)[puts it at 30 bytes after starting of file] eg: file.seek(-30,2)[puts it at 30 bytes before the end of the file]
#file.tell() - Gives current pointer location. If its at beginning, tell will give some hexadecimal value(but it says 0). At next record reading, it gives 1 and so on
#c:\Users\\raghu\\OneDrive\\Desktop\\Programs...... - Absolute path OR Pathname(Complete path from the root directory)(double dot ..)
#If file is in different FOLDER, give complete path while opening
#just the file name('goat.txt') - Relative path(relative to the current working directory)(single dot . )
#Text files can have /r,/n or both as EOL characters 
#Each line of text is terminated with a special character called EOL character(End of Line)
#Text files store information in both ASCII and Unicode

#Binary files are stored as a stream of bytes, so its faster(Information is stored in 0s and 1s)
#Images and audio can also be stored here
#Binary files store huge amt of info
#Text files have EOL character translations or delimiters which is not there in binary files making it faster(No EOL or any translations)
#A slight change in the binary file will corrupt it, while text files are not like that
#Serialization OR Pickling - list(or any other) object is converted into byte streams
#Deserialization OR Unpickling - Byte strings converted into list(or any other) objects
#After every load, the pointer shifts forward once
#dumps(object, pickleProtocol=None, *, fix_imports=True) #returns the 'bytes' object for the pickled python object

#CSV Files. [Comma Seperated Value Files][Default Delimiter]
#CSV files are also called Flat files
#They can be operated by any spreadsheet software as well as notepad!!
#Its neatly displayed in rows and columns. The file is easier to import and export and is preferred in database storage. Easier to create
#Other delimiters like ->(tab),pipe(|) and tilde(~) can also be used
#A row is left between 2 rows, as by default a newline character is there. Translation takes TIME, THATS WHY we use newline = '' (suppresses EOL translation)
#csv.writer(file) data is written on this writer object which converts user data into delimited form and writes it onto the csv file
#csv.reader(file) loads the data from the csv file, parses it(removes delimiters) and returns the data in the form of a python iterable

import csv,pickle,os,sys
'''
file = open('goat.txt','w')
file.truncate(20) #Only allows 20 bytes in the file(bogus letters that cant be printed)
'''
'''
file = open('goat.txt','w') #Writing file
file.write('hoho') #CANT print int or list type
file.write('hello') #Info is written CONTINUOSLY - hohohello
file.close()
'''
'''
file = open('goat.txt','w')
file.write("holo\nhello")
file.close()
'''
'''
file = open('goat.txt','r') #Reading file
x = file.read(2) #Number of characters
print(x)
x = file.read(3) #Pointer was at #2, so it will continue reading from last pointer.
print(x)
file.close()
'''
'''
file = open('goat.txt','r')
for c in file.read(): #One character at a time
    print(c,end = '')
file.close()
'''
'''
file = open('goat.txt','r')
for c in file.read().split(): #Words at a time
    print(c)
file.close()
'''
'''
file = open('goat.txt')# Reading by using the file object and not a function like read()
for i in file:#Even if it is in a for loop, the whole file is printed in one go
    print(i,"@@@")
print(file)#Prints file in un-understandable form
file.close()
'''
'''
file = open('goat.txt')
print(file.readline()) # Reading line by line[Here it is the first line]. Pointer moves to next line now
                       # If you give file.readline(2) [Only first 2 characters of the first line]
                       # If you give file.readline(100) [It will only maximum read the whole line. EOL feature]
#To read all lines
var = file.readline()
while var: #Prog stops when it hits a blank line
    print(var) #if var[0] == 'L': #characters of the line can be accessed by index
    var = file.readline()

file.close()
'''
'''
file = open('goat.txt')
print(file.readlines()) # prints all the lines in a LIST like ['hello\n','hoho']
print(file.readlines(0)) # prints all the lines in a LIST like ['hello\n','hoho']
print(file.readlines(4)) # If 4 bytes gets over in first line, then only first line, else it will print first two lines, if that also over, then 3rd line it will go to
print(file.readlines(-2)) #ERROR
print(file.read(-1)) #prints everything in the file
file.close()
'''
'''
file = open('goat.txt','w')
file.writelines(["welcome","hello"]) #Another way of writing. Elements of list are written CONTINUOSLY
file.close()
'''
'''
with open('goat.txt','a') as file: #Now you dont need to close the file
      file.write('Hello')
'''
'''
file = open('goat.txt','w+')
sen = ''
while True:
        s = input("Enter the sentence:")
        sen = sen + '\n' + s
        z = input("Enter 'y' to continue:")
        if z != 'y':
            break
file.write(sen)
file.seek(0)
for c in file.readlines():
      print(c)
file.close()
'''
'''
file = open("goat.txt", "r")
for line in file:
    print(line[0], end="")
'''
'''
file = open("out.txt", "w+")
s = "this"
print(s, "is a test", file=file)
file.seek(0)
print(file.read())
file.close()
'''
'''
file = open('goat.txt')

var = file.readlines()
l = []
for c in var:
    if 'a' in c:
        l.append("the letter 'a' was here\n")
    else:
        l.extend([c,"\n"])
file.close()

file = open('goat.txt','w')

for c in l:
    file.write(c)

file.close()
'''
'''
file = open('goat.txt','r+')
# If w+, file is erased and then it will proceed
d = {}
for c in file.read().split():
     if c in d:
         d[c] +=1
     else:
         d[c] = 1
maxx =  ''
for c in d:
    if d[c] == max(d.values()):
        maxx = c
file.writelines(["\n","Word: ",str(maxx),"\n","Frequency: ",str(max(d.values()))])

file.close()
'''
'''
file = open('goat.txt',"r+")
words = file.read().split()
u = input("Enter the userid:")
while True:
    if u in words:
        u = input("Invalid id, please enter a valid ID:")
    else:
        break
file.seek(0)
file.write(u+'\n')
file.close()

file = open('goat.txt','a')
p = input("Enter the password:")
d = False
while not d:
    if len(p) > 7:
        for c in p:
            if c in ['@','$','%']:
                d = True
                break
        else:
            p = input("Enter a valid password:")
    elif d:
        break
    else:
        p = input("Enter a valid password:")

file.write(p)
file.close()

'''
'''
z = input("Enter the file name:")
while True:
    try:
        file = open(str(z))
    except:
        z = input("Enter a valid file name with suffix:")
    else:
        break
for c in file.readlines():
    print(c.upper())
file.close()
'''
'''
file = open('goat.txt')
sen = ''
for c in file.read():
    if c.isupper():
        sen = sen + c.lower()
    elif c.islower():
        sen = sen + c.upper()
    else:
        sen = sen + c
new = open('rabbit.txt','w')
new.write(sen)
new.close()
file.close()
'''
'''
with open('fj.csv','w',newline = '') as file: #.csv File Extension
    a = csv.writer(file) # Writer object created
    t = ['Roll No ','Name','Marks'] # Simply we are giving for header
    a.writerow(t)
    l = [1,'John',23]
    a.writerow(l) # It writes only lists and dictionaries. After writing, it leaves a row and then prints next
                  # If newline = '' is given, it doesnt leave a line
    l = [2,'Mary',43]
    a.writerow(l)
'''
'''
with open('fj.csv','w',newline = '') as file:
    a = csv.writer(file)
    l = [[1,'John',23],[2,'Mary',43]]
    a.writerow(l) # The list is printed in ONE line.
                  #In the excel sheet, it is stored like this - [1,'John',23](in first cell) and then [2,'Mary',43](in second cell)
    a.writerows(l) # The nested list is printed properly. Writerows takes each list in the list to be printed in seperate rows

with open('fj.csv','r',newline = '') as file: #newline is waste here, you are only reading
    a = csv.reader(file) #'a' has COMPLETE record in the file
    print(next(a)) #Basically returns current record and moves pointer to the next record
    print(next(a))
    print(next(a))
    for c in a: #HAVE to iterate to print
        print(c) #Printing happens with everything in string. Each list will be in one line. All numbers will also be converted into strings
'''
'''
with open('fj.csv','w',newline = '') as file:
    a = csv.writer(file,delimiter = "\t") #Changing delimiters
    l = [1,'John',23]
    a.writerow(l)
    l = [2,'Mary',43]
    a.writerow(l)
with open('fj.csv','r',newline = '') as file:
    a =  csv.reader(file,delimiter = "\t") # If delimiter = "\t" is not given. Print will be like ['1\tJohn\t23']
#                                                                                                 ['2\tMary\t43']
    for c in a:
        print(c)
'''
'''
with open("newb.dat",'wb') as file:
    print(os.getcwd()) #Gives current working directory(FULL)
    a = os.getcwd()
    print(os.path.exists(a)) #This path exists
    a = a + '\\nNewb.dat'
    print(os.path.exists(a)) # This path is some random stuff we made
    os.mkdir('folder1') # Making directories.
    os.chdir('folder1') # Changing directories to that current one
    print(os.getcwd())

try:
    file = open('nNewb.dat','rb')  #opening a file in read mode that doesnt exist
except IOError: #Or except FileNotFoundError:
    print('File not found')
with open('9b.dat','rb') as file:
    print(file.closed) #ATTRIBUTE NOT FUNCTION #checks whether file is closed or not
    print(file.name) #Gives file's name
    print(file.mode) #Gives file's mode
'''
'''
#SYS MODULE

x = sys.stdin.readline() #Input given
sys.stdout.write(x) #Output given

x = sys.stdin.read() #Number denotes how many bytes need to be read. If number of bytes are not given it will keep reading
sys.stdout.write(x)

#stderr - same as stdout, but will display only errors on the device
#sys.stdin() is advantageous when number of bytes need to be specified
'''
'''
#BINARY ENCODE DECODE
with open('newf.dat','wb+') as file:
    a = 'Hello World' #Only strings can be used here. No dict and lists, thats why we use dump more
    file.write(a.encode()) #String to byte stream, Written in me readable form
    file.seek(0)
    z = file.read()
    print(type(z)) #Will give <class 'bytes'>
    print(z) #Will be preceded by a 'b'
    print(z.decode()) #Will print normally
'''
'''
with open ('rabbit.txt','r') as file:
    sen = ''
    for c in file.read().split('\n'):
        for d in c.split():
            if d.startswith('I'):
                sen = sen + ' ' + d[::-1]
            else:
                sen = sen + ' ' + d
        sen += '\n'        
    print(sen)            
'''
'''  
with open('rabbit.txt', 'r') as file:
        sen = ''
        for c in file.readlines():
            for d in c.strip('\n').split():
                if d.startswith('I'):
                    sen = sen + ' ' + d[::-1]
                else:
                    sen = sen + ' ' + d
            sen = sen + '\n'
        print(sen)
'''        
'''
with open ('rabbit.txt','r') as file:
    sen = ''
    var = file.readline()
    while var:
        d = var.strip('\n').split()
        for c in d:
            if c.startswith('I'):
                sen = sen + ' ' + c[::-1]
            else:
                sen = sen + ' ' + c
        sen = sen + '\n'    
        var = file.readline()    

    print(sen)
'''
'''
with open ('rabbit.txt','r') as file:
    var = file.readline()
    count = 0
    while var:
        if var[0].islower():
            print(var)
            count +=1
        var = file.readline()
    print(count)
'''         
'''
with open('rabbit.txt','r') as file:
    l = [i for i in file.readlines() if i.strip('\n')[0].islower()]
    c = len(l)
    for d in l:
        print(d.strip('\n'))
    print(c)    
'''
'''
with open('rabbit','r') as file:
    var = file.readline()
    maxx = ''
    while var:
        if len(var) > len(maxx):
            maxx = var
        var = file.readline()
    print(maxx)
'''
'''
with open ('rabbit.txt','r') as file:
    maxx = ''
    for i in file.readlines():
         if  len(i) > len(maxx):
            maxx = i
    print(maxx)         
'''
'''
with open ('rabbit.txt','r') as file:
    var = file.readline()
    maxx = ''
    while var:
        if len(var) > len(maxx):
            maxx = var
        var = file.readline()
    print(maxx)        
'''
'''
with open ('rabbit.txt','r') as file1:
    with open ('goat.txt','w') as file2:
        x = file1.readlines() 
        for i in x:
            if not i[0].islower():
                file2.write(i)
'''
'''
with open ('upper.txt','w') as file1:
    with open ('lower.txt','w') as file2:
        with open ('others.txt','w') as file3:
            while True:
                inp = input("Enter character: ")
                if inp.islower():
                    file1.write(inp)
                elif inp.isupper():
                    file2.write(inp)
                else:
                    file3.write(inp)
                y = input("Enter 'y' to continue: ")
                if y != 'y':
                    break
'''
'''
sen =  ''
with open ('rabbit.txt','r') as file:
    for c in file.read():
        sen = c + sen
print(sen)        
'''
'''
#creates another file but every blank space is a dollar sign
with open ('rabbit.txt','r') as file1:
    with open ('others.txt','w') as file2:
        for c in file1.read():
            if c == '\n':
                file2.write('\n')
            elif c.isspace():
                file2.write('$')   
            else:
                file2.write(c)    
'''                
'''
#roll  no name marks, given rollno display info
l = []
while True:
    roll = int(input("Enter the roll number: "))
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    print()
    l.append(str(roll) + ' ' + name + ' ' + str(marks) + '\n' )
    y = input("Enter 'y' to continue: ")
    if y != 'y':
        break
file1 = open('upper.txt','w')
file1.writelines(l)
file1.close()
print()
x = input("Enter the Roll Number:")
with open ('upper.txt','r') as file:
    for c in file.readlines():
        if c.split()[0] == x:
            print(c)
'''
'''
ch = input("Enter the character to check: ")
with open ('rabbit.txt','r') as file:
    for c in file.read().split('\n'):
        if c[-1] == ch:
            print(c)
'''         
'''   
count = 0
with open('rabbit.txt','r') as file:
    for c in file.read().split():
        if len(c) == 3:
            count+=1
print(count)            
'''
'''
ca = ce = ci = co = cu = 0
with open('rabbit.txt','r') as file:
    for c in file.read():
        if c.lower() == 'a':
            ca+=1
        elif c.lower() == 'e':
            ce +=1
        elif c.lower() == 'i':
            ci +=1
        elif c.lower() == 'o':
            co +=1
        elif c.lower() == 'u':
            cu +=1
print(' a - ',ca,' e - ',ce,' i - ',ci,' o - ',co,' u - ',cu)            
'''
'''
with open('rabbit.txt','r') as file:
    d = {}
    for c in file.read().split():
        try:
            if d[c]:
                d[c] +=1
            else:
                d[c] = 1
        except KeyError:
            d[c]+=1        
print(d[max(d.values())],max(d.values()))                
'''
#BINARY REVISION
'''
with open('rabbit.dat','rb') as file:
    count = 0
    try:
        while True:
            a = pickle.load(file)
            if a[2] == 'A':
                count+=1
    except EOFError:
        pass 
    print(count)           
'''
'''
with open('rabbit.dat','rb') as rfile:
    with open('writer.dat','wb') as wfile:
        ml = []
        try:
            while True:
                a = pickle.load(rfile)
                if a[1][0] in 'Ss':
                    ml.append(a)
        except EOFError:
            pass
         pickle.dump(ml,wfile) 

'''
'''
with open('rabbit.dat','wb') as file:
    d = {}
    while True:
        d['icode'] = int(input("icode: "))
        d['Name'] = input("Name: ")
        d['Price'] = int(input("Price: "))
        pickle.dump(d)
        z = input("Enter 'y' to continue: ")
        if z != 'y':
            break
'''
'''
a = {'icode':100,'Name':'Pencil','Price':10.0}
b = {'icode':101,'Name':'Pen','Price':90.0}
c = {'icode':102,'Name':'Colours','Price':150.0}
with open('rabbit.dat','wb') as file:
    pickle.dump(a,file)
    pickle.dump(b,file)
    pickle.dump(c,file)

with open('rabbit.dat','rb+') as file:
    try:
        while True:
            t = file.tell()
            a = pickle.load(file)
            a['Price'] = 1.1*a['Price']
            file.seek(t,0)
            pickle.dump(a,file)
    except EOFError:
        pass    
'''    
'''
with open('rabbit.dat','rb') as file:
    count = 0
    try:
        while True:
            a = pickle.load(file)
            count += a['Price']
    except EOFError:
        pass        
    print(count)
'''
'''                  
with open ('rabbit.dat','wb') as file:
    while True:
        Bn = int(input("Enter the book number: "))
        BN = input("Enter the BookName: ")
        An = input("Enter the author name: ")
        l = [Bn,BN,An]
        pickle.dump(l,file)
        z = input("Enter 'y' to continue: ")
        if z != 'y':
            break
name = input("Enter name: ")
count = 0        
with open('rabbit.dat','rb') as file:
    try:
        while True:
            a = pickle.load(file)
            if [2] == name:
                count+=1
    except EOFError:
        pass
print(count)   
'''
'''                     
with open('rabbit.dat','rb') as rfile:
    with open ('sports.dat','wb+') as wfile:
        try:
            while True:
                a = pickle.load(rfile)
                if a[1] == 'd':
                    pickle.dump(a,wfile)
        except EOFError:
            pass
    wfile.seek(0)
    print(pickle.load(wfile))
'''
'''
with open('writer.dat','rb') as file:
    try:
        while True:
            a = pickle.load(file)
            if a[2] > 75:
                print(a)  
    except EOFError:
        pass    

auth = 'frog'
count = 0
with open('writer.dat','rb') as file:
    try:
        while True:
            a = pickle.load(file)
            if a[2] == auth:
                count +=1
    except EOFError:
        pass    
'''
#CSV REVISION
'''
with open ('animals.csv','w',newline='') as file:
    a = csv.writer(file)
    ml = [['Family','Species','Habitat'],['Mammals','Tiger','Forest'],['Fishes','Shark','Ocean'],['Birds','Sparrow','Countryside']]
    a.writerows(ml)
with open('animals.csv','r') as file:
    a = csv.reader(file)
    next(a)
    for c in a:
        if c[0] == 'Mammals':
            print(c)
'''


 
