x=int(input()) #x는 첫번째 피연산자
egg(x)
op = input() #op는 연산자

while(op!='='): #연산자가 =이 나오기전까지 반복연산
    y=int(input()) 
    egg(y)
    if (op == '+'): 
        x += y 
    elif (op == '-'): 
        x -= y 
    elif (op == '*'): 
        x *= y 
    op = input() 
    
print(x) #출력

def egg(num):    #이스터에그 함수, 함수에 정수하나 입력 받아서 해당 수가 특이한 숫자일 경우 문장 출력
    if(num==7):
        print("행운")
    elif(num==1221):
        print("종강종강 돌을 던지자")
    elif(num==18):
        print("바른말고운말")
    elif(num==0):
        print("0은 여기서 False란다")
    elif(num==1):
        print("1은 여기서 True란다")
    elif(num==2):
        print("Binary..?")
    elif(num==534):
        print("컴공생들의 무덤")


