'''
--Program 17--

Write a program to convert infix notation to postfix notation using stacks.
'''

ops = ['+','-','*','/','^','(',')']
prec = {'(':0,')':0,'+':1,'-':1,'*':2,'/':2,'^':3}

while True:
    exp = input("Enter the expression: ")
    print()
    stk = []
    final_exp = ''
    for c in exp:
        if c not in ops:
            final_exp += c
        else:
            if c == '(':
                stk.append(c)
            elif c == ')':
                while True:  # (in brackets, when you encounter closing bracket, pop all aperators and add it to the end of brackets)
                    if stk:
                        d = stk.pop()
                        if d != '(':
                            final_exp += d
                        else:
                            break
            else:        
                if stk:               
                    # Operators go into stack(first if a higher priority operatoris there and a lower wants to come, you pop the higher dude and enter the lower pririty one
                    if prec[c] > prec[stk[-1]]:
                        stk.append(c)    
                    else:
                        final_exp += stk.pop()
                        stk.append(c)
                else:
                    stk.append(c)
    for c in stk[::-1]:
        final_exp += c                    
    print(final_exp, '\n')

    z = input("Enter 'y' to continue: ")
    print()
    if  z != 'y':
        print("Exiting now...")
        break
