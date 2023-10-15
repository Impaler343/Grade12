def linear():
    m = None
    x = [int(i) for i in input("Enter the list: ").split(' ')]
    print()
    k = int(input("Enter the number to be found: "))
    for i in range(len(x)):
        if x[i] == k:
            m = i
            break
    else:
        print("\nThe number was not found")
    if m:
        print("\nThe number",x[m],"was found at index:",m)    
def binary():
    f = None
    x = [int(i) for i in input("Enter the list: ").split()]
    print()
    k = int(input("Enter the number to be found: "))
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]

    end = len(x)-1
    start = 0
    while start <= end:
        mid = int((end + start)/2)
        if k == x[mid]:
            f = mid
            break
        elif x[mid] > k:
            end = mid -1
        elif x[mid] < k:
            start = mid + 1
    else:
        print("The number was not found")
    if f:
        print("The number",x[f],"was found at index:",f)    


while True:
    print('''
    #1 Linear Search
    #2 Binary Search
    #3 Exit
    \n''')
    z = input("Enter your choice: ")
    if z == '1':
        linear()
    elif z == '2':
        binary()
    elif z == '3':
        print("Exiting now...")
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #linear calls input function
    #for binary calls input function and  input in asc