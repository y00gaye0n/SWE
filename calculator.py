while True:
    # 사용자에게 숫자 입력 받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    operator = input("사칙연산 중 하나를 입력하세요 (+, -, *, /): ")
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 입력된 연산자에 따라 계산 수행
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
            continue
    else:
        print("올바르지 않은 연산자입니다.")
        continue

    # 결과 출력
    print("결과: {:.2f}".format(result))

    # 계속할지 여부 확인
    another_calculation = input("더 계산하시겠습니까? (y/n): ")
    if another_calculation.lower() != 'y':
        print("프로그램을 종료합니다.")
        break
