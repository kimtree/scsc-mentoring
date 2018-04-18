import random


def generate_random_number():
    return str(random.randint(100, 999))


def get_game_result(user_number_str, answer_number_str):
    strike = 0
    ball = 0

    # 3자리 숫자임을 가정해서 range(3)
    for i in range(3):
        # 정답과 일치하는 숫자가 있는 경우
        if user_number_str[i] in answer_number_str:
            if user_number_str[i] == answer_number_str[i]:
                # 정답과 일치하는 숫자가 위치도 일치하는 경우
                strike += 1
            else:
                # 위치가 일치하지 않는 경우
                ball += 1

    # 다 맞춘 경우
    if strike == 3:
        print('Yes! The secret number is "' + answer_number_str + '"! You have won!')
        print()
        return True

    # 다 맞추지 못한 경우
    print(str(strike), 'strike,', str(ball), 'ball.')
    print()
    print('==========' * 3)

    return False


def main():

    # 랜덤 숫자 생성
    answer = generate_random_number()

    # 시작 문구 표시
    print('S T A R T')
    print('==========' * 3)

    while True:
        print('Guess numbers (000 ~ 999):')
        # 유저 숫자 입력
        user_answer = input()

        # 겹치는 숫자 다 맞췄는지 결과 리턴
        game_result = get_game_result(user_answer, answer)

        # 겹치는 숫자 맞춘 경우는 다시 게임할 것인지 물어봄
        if game_result:
            user_input = input('Do you want to play again? (yes or no)')
            if user_input == 'no':
                break
            else:
                # 새 랜덤 숫자 생성
                answer = generate_random_number()


if __name__ == '__main__':
    main()
