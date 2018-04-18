def get_user_input():
    print('Please input the last number')
    number = int(input())

    return number


def print_369_until(number):
    print('-' * 20)

    # 1 부터 number까지
    for i in range(1, number + 1):
        is_contains_369 = False

        # 숫자를 문자열로 변환 후 한자리씩 리턴
        for j in str(i):
            # 3, 6, 9가 j안에 포함되어있는 경우
            if j in ['3', '6', '9']:
                print('clap ', end='')
                is_contains_369 = True

        # 3, 6, 9가 포함 안 된 경우만 숫자 출력
        if not is_contains_369:
            print(i)
        else:
            print()


def main():
    number = get_user_input()

    print_369_until(number)


if __name__ == '__main__':
    main()
