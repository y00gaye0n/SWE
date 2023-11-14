egg(x):
    if(x=7):
        print("행운")
    elif(x=1221):
        print("종강종강 돌을 던지자")
    elif(x=18):
        print("바른말고운말")
    elif(x=0):
        print("0은 여기서 False란다")
    elif(x=1):
        print("1은 여기서 True란다")
    elif(x=2):
        print("Binary..?")
    elif(x=534):
        print("컴공생들의 무덤")

x=int(input())
egg(x)
op = input()

while(op!='='):
    y=int(input())
    egg(y)
    if (op == '+'):
        x += y
    elif (op == '-'):
        x -= y
    elif (op == '*'):
        x *= y
    op = input()
    
print(x)
