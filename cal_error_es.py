
error = 0
try:
    x = int(input())
except ValueError:
    x = 0
    error += 1

op = input()

while (op != '='):
    try:
        y = int(input())
    except ValueError:
        y = 0
        error += 1

    if (op == '+'):
        x += y
    elif (op == '-'):
        x -= y
    elif (op == '*'):
        x *= y

    op2 = input()
    if (op != op2):
        op = op2
        if (op != '='):
            error += 1

if (error > 0):
    print("ERROR!")
else:
    print(x)

