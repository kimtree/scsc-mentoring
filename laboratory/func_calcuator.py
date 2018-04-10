# 덧셈 함수
def add(a, b):
    return a + b


# 뺄셈 함수
def sub(a, b):
    return a - b


# 곱셈 함수
def mul(a, b):
    return a * b


# 나눗셈 함수
def div(a, b):
    return a / b


def display_intro():
    print('operator(+, -, *, /, exit)')


def get_operand():
    print('operand')
    value = input(' >> ')

    return float(value)


def display_result(result):
    print('result')
    print('--------------------')
    print('>>>', str(result))
    print('--------------------')


def main():
    print('first operand is 0')

    operand1 = 0.0  # float
    result = 0.0

    display_intro()
    operator = input(' >> ')

    while True:
        if operator == '+':
            operand2 = get_operand()
            result = add(operand1, operand2)
        elif operator == '-':
            operand2 = get_operand()
            result = sub(operand1, operand2)
        elif operator == '*':
            operand2 = get_operand()
            result = mul(operand1, operand2)
        elif operator == '/':
            operand2 = get_operand()
            result = div(operand1, operand2)
        elif operator == 'exit':
            print('계산기를 종료합니다.')
            break  # while loop를 탈출
        else:
            print('올바르지 않은 입력입니다.')

        display_result(result)

        operand1 = result  # 첫번째 연산 결과를 다음번 연산의 첫번째 인수로 전달

        display_intro()
        operator = input(' >> ')


if __name__ == '__main__':
    main()
