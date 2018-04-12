from math import log10
import string


def chosen_plaintext_attack(plaintext, ciphertext, bifurcation, texttodecrypt):
    pass
#딕셔너리 사용
#h                ┌Key--------------------------------------┐ : ┌Value--┐
#h  dictionary = {ciphertext[n*bifurcation : (n+1)*bifurcation] : plaintext[n]}

#출력 형식
#h  "\n해독된 텍스트: "
#h  "\n암호 해독이 중단되었습니다. 찾을 수 없는 키: "

    # TODO: 딕셔너리에 암호문(ciphertext)를 bifurcation만큼 자름
    # TODO: 자른 암호문(ciphertext)을 -> 평문값(plaintext) 1자에 대응하는 딕셔너리 생성

    # TODO: 해독할 텍스트(texttodecrypt)를 bifurcation 만큼 자름
    # TODO: 자른 텍스트(texttodecrypt)로 딕셔너리에 key가 있는지 확인

    # TODO: 딕셔너리에 키를 못 찾은 경우(try~except)는 '암호 해독이 중단 되었습니다. 찾을 수 없는 키' 출력 후 종료
    # TODO: 딕셔너리에서 키를 찾아서 해독이 가능한 경우는 해독된 문자열을 출력


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

    quadDic = {}
    while True:
        line = fp.readline()
        if not line: #파일의 내용을 한줄씩 읽고 다음줄이 없으면 while문 break
            break

        # TODO: line 함수는 텍스트 파일에서 읽어온 한 줄의 텍스트가 들어있음
        # TODO: (while loop가 한 턴 지나면 다음 줄 값이 들어옴)

        # TODO: 읽어온 한 줄의 텍스트를 나눔 (split)

        # TODO: 딕셔너리에 quadgram을 key로 하고, 값으로 list[]를 만들어서 [count, log_probabilty] 생성
        # TODO: 이 때 count, log_probabilty는 int형 자료형이 맞는지 확인, 그렇지 않으면 변환
        # TODO: quadDic = { 'TION': [10292939, 0], 'QUAD': [19323333, 0]}

        # TODO: 전체 quadgram count의 합 계산

#   열었던 파일을 닫음
    fp.close()

#h  log probability 값 계산해서 딕셔너리에 추가
    for key in quadDic:
        pass
        # TODO: quadgram의 count를 전체 quadgram count의 합으로 나눈 것을 log10을 취한 값을 계산
        # TODO: quadDic에 quadgram을 key로 하는 list를 꺼내서, log_probabilty 값을 업데이트함
        # TODO: quadDic = { 'TION': [10292939, -2.718283] - 0에서 새 값으로 업데이트 됨, 'QUAD': [19323333, -2.718283]}

#출력 형식
    print("\n{:<8s}{:>13s}{:>22s}".format('Quadgram','Count','Log Probability'))
    print("-------------------------------------------")
#h  "{:<8s}{:>13d}{:>22.6f}".format( -해당값- , -해당값- , -해당값- )

    # TODO: quadDic의 값을 list로 옮겨 담은 후, count가 높거나, log_probability가 낮은 순으로 정렬
    # TODO: list.sort() 함수는 리스트의 첫번째 인자를 기준으로 정렬함
    # TODO: 정렬된 list에서 TOP 10개만 잘라서 아래 출력 형식에 맞추어 출력함

    # TODO: 이 함수는 계산된 quadDic 값을 리턴해야함


def bruteforce_shift_cipher(ciphertext, quadgram_dictionary):
    # TODO: (참고) 혹시 값이 이상하면 ciphertext를 대문자로 변경 필요

    # TODO: 0부터 25번까지 (알파벳 갯수: 26) ciphertext를 한 칸씩 이동함
    # TODO: 이동할 때는 shift_characters 함수를 사용
    # TODO: 예시) ABCD(0번) -> BCDE(1번) -> CDEF(2번)

    # TODO: 변환된 ciphertext를 이용하여 fitness_calculator 함수를 호출하여 fitness 값을 계산
    # TODO: 변환된 ciphertext와 key와 fitness 값을 리스트에 담아둠

    # TODO: fitness 값이 높은 순서대로 정렬하여 5개만 출력

#출력 형식
    print("{:<5s}{:^35s}   {:>10s}".format("\nKey", "Plaintext", "Fitness"))
    print("------------------------------------------------------")
#h  "{:<5d}{:^35s}   {:>10.4f}".format( -해당값- , -해당값- , -해당값- ))

    # TODO: 해독된 암호문은 fitness 값이 높은 최종 결과 1개만 출력
#h  "\n계속하려면 엔터키를 누르세요..."
#h  "\n해독된 암호문: "



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
    # TODO: potential_plaintext를 quadgram(4)글자 단위로 자름

    # TODO: 추출한 quadgram을 quadgram_dictionary의 key로 값을 찾은 후에 log_probability를 가져옴
    # TODO: quadgram_dictionary에 key가 없는 경우는 무시

    # TODO: log_probabilty 값을 전부 더해서 결과로 리턴함
    pass
#매개변수로 받은 potential_plaintext를 qardgrams으로 나눠서
#모든 qardgram의 log_probability들의 합을 리턴
#       ex) potential_plaintext = 'PYTHON' 일때 qardgrams은 ‘PYTH',‘YTHO,‘THON’



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


#h  "선택: "
#h  "입력이 올바르지 않습니다."
#h  "평문: "         -> plaintext
#h  "암호문: "       -> ciphertext
#h  "분기: "         -> bifurcation
#h  "해독할 문장: "  -> texttodecrypt


#h  2번 문자 빈도 분석에서 bruteforce_shift_cipher()함수 호출을 위한 ciphertext 공백, 구두점 제거
#h  ciphertext = ciphertext.replace(' ', '').translate(str.maketrans({key: None for key in string.punctuation}))



#Execute the main() function
if __name__ == "__main__":
    main()
