import random
import time

print('*' * 7, 'START', '*' * 7)

max_iter = 5
i = 0
while i < max_iter:
	# 1부터 9까지의 임의의 숫자를 리턴함
	num_1 = random.randint(1, 9)
	num_2 = random.randint(1, 9)
	num_3 = random.randint(1, 9)
	num_4 = random.randint(1, 9)
	correct_answer = num_1 * num_2 + num_3 - num_4

	print(str(num_1), '*', str(num_2), '+', str(num_3), '-', str(num_4),  '= ?')

	# 3초간 프로그램을 정지하고 카운트 출력
	count = 1
	while count <= 3:
		time.sleep(1)
		# flush=True 옵션을 주지 않으면 time.sleep시에는 print함수의 결과가 화면에 바로바로 표시 되지 않음
		print(str(count) + ', ', end='', flush=True)
		count += 1

	print(': ', end='')
	answer = int(input())

	if answer == correct_answer:
		print('Correct Answer')
	else:
		print('Wrong Answer,', str(num_1), '*', str(num_2), '+', str(num_3), '-', str(num_4), '=', str(correct_answer))

	i += 1
