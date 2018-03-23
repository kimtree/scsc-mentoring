# 모래시계 모양 피라미드
n = int(input('number:'))

i = 0
while i < n - 1:
    print('  ' * i, ' *' * (2*(n-i)-1), end='')
    i += 1
    if i != n - 1:
        print('\n', end='')

i = 0
while i <= n:
    print('  ' * (n-i), ' *' * (2*i-1))
    i += 1
