x=int(input()) #x는 첫번째 피연산자

op = input() #op는 연산자

while(op!='='): #연산자가 =이 나오기전까지 반복연산
    y=int(input()) 

    if (op == '+'): 
        x += y 
    elif (op == '-'): 
        x -= y 
    elif (op == '*'): 
        x *= y 
    op = input() 
    
print(x) #출력
