while True:
    # 사용자에게 숫자 입력 받기
    x = int(input("첫 번째 숫자를 입력하세요: "))
    operator = input("사칙연산 중 하나를 입력하세요 (+, -, *): ")
    y = int(input("두 번째 숫자를 입력하세요: "))

    # 입력된 연산자에 따라 계산 수행
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y
    else:
        print("올바르지 않은 연산자입니다.")
        continue
    
    # 결과 출력
    print("결과:", result)
