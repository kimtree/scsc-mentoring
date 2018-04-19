from math import log10
import string


def chosen_plaintext_attack(plaintext, ciphertext, bifurcation, texttodecrypt):
#딕셔너리 사용
#h                ┌Key--------------------------------------┐ : ┌Value--┐
#h  dictionary = {ciphertext[n*bifurcation : (n+1)*bifurcation] : plaintext[n]}

#출력 형식
#h  "\n해독된 텍스트: "
#h  "\n암호 해독이 중단되었습니다. 찾을 수 없는 키: "

    # 딕셔너리 초기화
    dictionary = {}

    # 암호문을 어디까지 잘랐는지 위치
    cipher_index = 0

    # 평문을 한글자씩 이동하면서 1개의 평문자에 해당하는 암호문 글자를 가져와서 딕셔너리에 추가
    for text in plaintext:
        cipher_part_text = ciphertext[cipher_index:cipher_index + bifurcation]
        dictionary[cipher_part_text] = text
        # 암호문을 어디까지 잘랐는지 bifurcation 만큼 이동
        cipher_index += bifurcation

    # 해독된 암호문을 저장하는 리스트
    decoded_text = []

    # 해독되지 못한 암호문 리스트
    not_decoded_text = []

    # 0부터 bifurcation 간격으로 index 이동
    for i in range(0, len(texttodecrypt), bifurcation):
        # 해독해야 할 암호 문자열 가져오기
        part_of_cipher = texttodecrypt[i:i+bifurcation]

        if part_of_cipher in dictionary:
            decoded_text.append(dictionary[part_of_cipher])
        else:
            not_decoded_text.append(part_of_cipher)

    # 해독되지 못한 텍스트가 남아있는 경우
    if not_decoded_text:
        print('암호 해독이 중단되었습니다. 찾을 수 없는 키:', ' '.join(not_decoded_text))
    else:
        # 해독 성공한 경우
        print('해독된 텍스트:', ''.join(decoded_text))


#제공 함수
#file pointer 리턴 함수
def open_file():
    while True:
        fileName = input("파일 이름을 입력해 주세요: ")
        try:
            fp = open(fileName, 'r')
        except:
            print("파일을 열 수 없습니다. 다시 시도해주세요.\n")
        else:
            return fp



def log_probability_dictionary(fp):

#딕셔너리 사용
#h               ┌Key--┐ : ┌Value-(list 형식)---┐
#h  dictionary = {quadgram : [count, log_probability]}

#   pointer를 받은 파일을 한줄씩 읽어서 딕셔너리로 만드는 과정
#h  total count of Quadgrams 도 함께 계산

    # 딕셔너리 초기화
    quadDic = {}
    # 총 quadgram count 변수 초기화
    total_quadgram_count = 0
    while True:
        line = fp.readline()
        if not line: #파일의 내용을 한줄씩 읽고 다음줄이 없으면 while문 break
            break

        # \n 개행문자 제거
        line = line.strip()

        # 한 줄의 데이터를 빈 값을 구분으로 나눔
        quadgram_data = line.split(' ')

        # 딕셔너리에 quadgram을 key로 하고, 값 list 내에 count와, log_probability를 0으로 초기화
        quadgram = quadgram_data[0]
        quadgram_count = int(quadgram_data[1])
        quadDic[quadgram] = [quadgram_count, 0]

        # 총 quadgram count 증가
        total_quadgram_count += quadgram_count

#   열었던 파일을 닫음
    fp.close()

#h  log probability 값 계산해서 딕셔너리에 추가

    # log_probability 계산
    for key in quadDic:
        # log_probability는 quadgram을 key로 한 딕셔너리 내 값(리스트)의 두번째에 위치함
        quadDic[key][1] = log10(quadDic[key][0] / total_quadgram_count)

#출력 형식
    print("\n{:<8s}{:>13s}{:>22s}".format('Quadgram','Count','Log Probability'))
    print("-------------------------------------------")

    # 상위 10개의 quadgrams
    # TODO: 정렬 방식 변경??
    quadgram_list = []
    for k, v in quadDic.items():
        quadgram_list.append([k, v[0], v[1]])

    quadgram_list.sort(key=lambda x: x[1])
    quadgram_list.reverse()

    # quadgram list를 10개까지만 출력
    for quadgram, count, log_probability in quadgram_list[:10]:
        print("{:<8s}{:>13d}{:>22.6f}".format(quadgram, count, log_probability))

    return quadDic


def bruteforce_shift_cipher(ciphertext, quadgram_dictionary):
    # 현재 저장된 quadgram이 대문자이므로 대문자로 변경
    potential_plaintext = ciphertext.upper()

    # fitness 리스트 초기화
    fitness_list = []

    # 0부터 25까지의 key 범위 지정
    for key in range(26):
        if key > 0:
            potential_plaintext = shift_characters(potential_plaintext)

        fitness = fitness_calculator(potential_plaintext, quadgram_dictionary)
        fitness_list.append([fitness, key, potential_plaintext])

    # fitness 값으로 정렬
    fitness_list.sort(key=lambda x: x[0])
    fitness_list.reverse()

#출력 형식
    print("{:<5s}{:^35s}   {:>10s}".format("\nKey", "Plaintext", "Fitness"))
    print("------------------------------------------------------")

    # 적합도 상위 5개의 리스트를 리턴
    for fitness in fitness_list[:5]:
        print("{:<5d}{:^35s}   {:>10.4f}".format(fitness[1], fitness[2], fitness[0]))

    # 엔터키 입력 대기를 input 함수로 대체
    input("\n계속하려면 엔터키를 누르세요...")

    # 리스트에서 적합도가 1위인 것을 가져와서 해독된 문자 출력
    print("\n해독된 암호문: ", fitness_list[0][2])


#제공 함수
#알파벳대문자 한칸씩 이동시키는 함수 ex) a -> b, b -> c, z -> a
def shift_characters(ciphertext):
    shiftedtext = ''
    for char in ciphertext:
        if ord(char) == 90:
            shiftedtext += chr(65)
        else:
            shiftedtext += chr(ord(char)+1)
    return shiftedtext



def fitness_calculator(potential_plaintext, quadgram_dictionary):
    # 매개변수로 받은 potential_plaintext를 qardgrams으로 나눠서
    # 모든 qardgram의 log_probability들의 합을 리턴
    #       ex) potential_plaintext = 'PYTHON' 일때 qardgrams은 ‘PYTH',‘YTHO,‘THON’

    quadgram_list = []
    for i in range(len(potential_plaintext) - 3):
        # i 위치 부터 4글자의 quadgram 추출
        quadgram = potential_plaintext[i:i + 4]
        quadgram_list.append(quadgram)

    quadgram_log_probability_sum = 0
    for quadgram in quadgram_list:
        # quadgram 딕셔너리에 값이 있는 경우에만 log probability 값을 더함
        if quadgram in quadgram_dictionary:
            log_probability = quadgram_dictionary[quadgram][1]
            quadgram_log_probability_sum += log_probability

    return quadgram_log_probability_sum


def main():
    BANNER = """\
    ---------------------------------------------------------------------
    
                암호 해독의 세계에 오신 여러분을 환영합니다.         
                
        이 프로그램은 암호 알고리즘이나 암호키에 대한 지식이 없더라도
          암호화된 암호문을 해독할 수 있게 도와주는 프로그램입니다.
    
    ---------------------------------------------------------------------
    """
    MENU = """\
    1. 선택 평문 공격 [chosen plaintext attack]
    2. 문자 빈도 분석 [quadgram frequency analysis]
    """

    # 메뉴 출력
    print(BANNER)
    print(MENU)

    while True:
        menu_input = input("선택: ")
        if menu_input == '1':
            plain_text = input('평문 : ')
            cipher_text = input('암호문 : ')
            bifurcation = int(input('분기 : '))
            text_to_decode = input('해독할 문장 : ')

            chosen_plaintext_attack(plain_text, cipher_text, bifurcation, text_to_decode)
            break
        elif menu_input == '2':
            # 파일 이름 입력 함수 호출
            fp = open_file()

            # quadgram 관련 정보 생성
            quadgram_dict = log_probability_dictionary(fp)

            cipher_text = input('암호문 : ')
            # 공백, 구두점 제거
            cipher_text = cipher_text.replace(' ', '').translate(str.maketrans({key: None for key in string.punctuation}))
            bruteforce_shift_cipher(cipher_text, quadgram_dict)
            break
        else:
            print('입력이 올바르지 않습니다.')


#Execute the main() function
if __name__ == "__main__":
    main()
