'''
--Program 18--

Write a program to evaluate postfix expression using stack.
'''

while True:
    exp = [i for i  in input("Enter the expression seperated by space: ").split()]
    print()
    stk = []
    opsb = {'+','-','*','/','**','&','|'}
    ans = None

    for c in range(len(exp)):
        if exp[c] in opsb:
            d = stk.pop()
            stk.append(eval(f"int({stk.pop()}){exp[c]}int({d})"))
        elif exp[c] == '~':
            stk.append(eval(f"{'~'}int({stk.pop()})"))
        else:
            stk.append(exp[c])     
    print('Evaluated Expression: ',stk[0],'\n')

    z = input("Enter 'y' to continue: ")
    print()
    if z != 'y':
        print("Exiting now...")
        break

