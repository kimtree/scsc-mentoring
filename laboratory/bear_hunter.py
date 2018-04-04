import random
import time

gaweibaweibo = ['가위', '바위', '보']

bear_index = 0
bear_names = ['아빠곰', '엄마곰', '아기곰']
bear_hp = [15, 10, 5]
bear_dam_range = [40, 20, 10]

bear_current_hp = 0
bear_dam = 0

my_hp = 40
my_current_hp = 0
my_dam = 0
my_bear_leather = 0

critical_dam = 15
round_number = 1


def display_hp_bar(name, max, current):
    # hp_bar_unit 단위로 바를 그려줌
    hp_bar_unit = 5

    current_hp_bar = int((current / hp_bar_unit))
    remain_bar = int((max / hp_bar_unit)) - current_hp_bar

    print('  ' + name + '  [', end='')
    print('=' * current_hp_bar + ' ' * remain_bar, end='')
    print('] ' + str(current) + '/' + str(max))


def display_intro():
    print('\n ========================ROUND ' + str(round_number) + '========================')
    time.sleep(1)
    display_hp_bar('Player', my_hp, my_current_hp)
    display_hp_bar(bear_names[bear_index] + '  ', bear_hp[bear_index], bear_current_hp)

    # print('      Player' + '   ' + bear_names[bear_index])
    # print('체력', end='')
    # print('    ' + str(my_current_hp) + '      ' + str(bear_hp[bear_index]))
    time.sleep(1)


def meet_bear():
    global bear_index, bear_current_hp
    bear_index = random.randint(0, 2)
    bear_current_hp = bear_hp[bear_index]

    global round_number
    round_number = 1

    print('\n어둡고 음침한 밤...')
    time.sleep(1)
    print('당신은 ' + bear_names[bear_index] + '을 만납니다!!!')
    time.sleep(1)


def game():
    print('\n가위바위보 중 하나를 선택 하십시오 [가위(1), 바위(2), 보(3)]')
    my_choice = int(input())
    bear_choice = random.randint(1, 3)

    print('       Player' + '   ' + bear_names[bear_index])
    print('선택', end='')
    print('    ' + gaweibaweibo[my_choice - 1] + '      ' + gaweibaweibo[bear_choice - 1] + '\n')

    if my_choice == bear_choice:
        game_result = 1
    else:
        if (my_choice == 1 and bear_choice == 3)\
            or (my_choice == 2 and bear_choice == 1)\
            or (my_choice == 3 and bear_choice == 2):
            game_result = 2
        else:
            game_result = 3

    # 치명타 확률 (20%)
    is_critical = (random.randint(1, 10) <= 2)
    if is_critical:
        min_dam = critical_dam
    else:
        min_dam = 1

    # 곰의 대미지 설정
    global bear_dam
    bear_dam = random.randint(min_dam, bear_dam_range[bear_index])

    # 나의 데미지 설정
    global my_dam
    my_dam = random.randint(min_dam, 38)

    # 라운드 넘버
    global round_number
    round_number += 1

    return game_result


def scoring(result):
    if result == 1:
        print('비겼습니다. 한 번 더!')
    else:
        if result == 2:
            if my_dam >= critical_dam:
                print(' >>>> Critical Hit!!!! <<<< ')
            print('이겼습니다!')
            time.sleep(1)
            print(bear_names[bear_index] + '을 공격하여 ' + str(my_dam) + '만큼의 데미지를 입혔습니다')
            # 곰 체력 깎기
            global bear_current_hp
            bear_current_hp -= my_dam

        elif result == 3:
            print('졌습니다 ㅜㅜ')
            time.sleep(1)
            print(bear_names[bear_index] + '이 당신을 공격하여 ' + str(bear_dam) + '만큼의 데미지를 입습니다')
            # 나의 체력 깎기
            global my_current_hp
            my_current_hp -= bear_dam


def get_gift():
    time.sleep(1)
    print('\n승리!!! 곰가죽을 얻었습니다')

    # 전리품 획득
    global my_bear_leather
    my_bear_leather += 1


def display_outro():
    print('\n ======================== 전리품 ========================')
    time.sleep(1)
    print(' >>>> 가죽을 ' + str(my_bear_leather) + '개를 획득했습니다!!')
    time.sleep(1)
    print('\n ====================== GAME OVER ========================')
    time.sleep(1)


my_current_hp = my_hp

while my_current_hp > 0:
    meet_bear()

    while my_current_hp > 0:
        display_intro()
        game_result = game()
        scoring(game_result)

        if bear_current_hp <= 0:
            get_gift()
            meet_bear()

    display_outro()



