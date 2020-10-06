#Basic Calculator in Python without any gui.

print("""
1. Only use '+' , '-' , '*' , '/'
2. Don't give space in between the expression.
3. Example Expression : 1+2*4+5-7
""")

while 1:
    c = 0
    exp = ['+','-','*','/']
    calc = input('Enter your Expression : ')
    for x in calc:
        if x.isdigit() or x in exp:
            c+=1
    
    if len(calc) == c:
        print(f'Answer is : {eval(calc)}')            
    else:
        print("Invalid Expression. Try again")

    if input('Do you want to exit(), Enter(Y/N): ').lower() == 'y':
        exit('Thanks for using calculator')
