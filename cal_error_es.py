
error = 0  
try:
    x = int(input()) #정수로 입력 받음 정수가 아닐 시 error 출력 
except ValueError:
    x = 0
    error += 1

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


if (error > 0):
    print("ERROR!")
else:
    print(x)
