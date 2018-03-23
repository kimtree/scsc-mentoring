# 가운데가 비어 있는 피라미드
n = int(input('number: '))

i = 1
while i <= n:
	print("  " * (n-i), end='')

	# 첫번째 줄과 마지막 줄이 아닌 경우 별을 빼야함
	if 1 < i < n:
		# 처음과 마지막 별을 제외
		print("* ", "  " * (2*i-4), "* ")
	else:
		print("* " * (2*i-1))

	i += 1
