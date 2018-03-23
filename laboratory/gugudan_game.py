import random
# import time

print('*' * 7, 'START', '*' * 7)

max_iter = 5
i = 0
while i < max_iter:
    # 1에서 9까지의 임의의 숫자를 리턴함
    dan_1 = random.randint(1, 9)
    dan_2 = random.randint(1, 9)

    print(str(dan_1), '*', str(dan_2), '= ?')
    # 3초간 프로그램을 정지
    # time.sleep(3)

    answer = int(input())

    if answer == (dan_1 * dan_2):
        print('Correct Answer')
    else:
        print('Wrong Answer,', str(dan_1), '*', str(dan_2), '=', str(dan_1 * dan_2))

    i += 1
