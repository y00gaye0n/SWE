def eggMessages(num):  # 이스터에그 함수, 함수에 정수하나 입력 받아서 해당 수가 특이한 숫자일 경우 문장 출
    if num == 7:
        print("행운")
    elif num == 1221:
        print("종강종강 돌을 던지자")
    elif num == 18:
        print("바른말고운말")
    elif num == 0:
        print("0은 여기서 False란다")
    elif num == 1:
        print("1은 여기서 True란다")
    elif num == 2:
        print("Binary..?")
    elif num == 534:
        print("컴공생들의 무덤")


error = 0
firstOperand = 0

try:
    firstOperand = int(input())  # x는 첫번째 피연산자
    eggMessages(firstOperand)
except ValueError:
    error += 1

operator = input()  # operator는 연산자

while operator != '=':  # 연산자가 =이 나오기 전까지 반복연산
    try:
        nextOperand = int(input())
        eggMessages(nextOperand)
    except ValueError:
        error += 1

    if operator == '+':
        firstOperand += nextOperand
    elif operator == '-':
        firstOperand -= nextOperand
    elif operator == '*':
        firstOperand *= nextOperand
    else:
        error += 1  # 더하기, 빼기, 곱하기 연산자 이외의 것일 경우 error 출력

    nextOperator = input()  # 다음 연산자 입력

    if operator != nextOperator :   # 동일한 연산인지 확인
        operator = nextOperator
        if operator != '=':
            error += 1

if error > 0:
    print("ERROR!")
else:
    print(firstOperand)  # 출력
