# input 함수로 값을 입력 받은 다음에 정수(int) 자료 형으로 변환
dan = int(input('Input dan.\n'))

# 문구 출력 ( '*' * 10 은 * 문자를 10개 반복하여 출력하라는 뜻 )
print('*'*10 + str(dan) + 'dan' + '*' * 10)

start_num = 1
max_num = 9
# 1단부터 9단까지 반복문
while start_num <= max_num:
	# 구구단 연산 결과 출력
	print(str(dan) + '*' + str(start_num) + '=' + str(dan * start_num))
	# 다음 loop 진행을 위해서 start_num 값을 증가시킴
	start_num += 1

# 마무리 문구 출력
print('*' * 24)
