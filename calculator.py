x=int(input())

op = input()

while(op!='='):
    y=int(input())

    if (op == '+'):
        x += y
    elif (op == '-'):
        x -= y
    elif (op == '*'):
        x *= y
    op = input()
    
print(x)
