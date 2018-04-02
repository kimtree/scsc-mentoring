import pprint

MAX_TRIES = 5

a = '''
------------|
            |
            |
'''

b = [1, '2', True, [3, '4', False]]
# print(b)
# print(b[2])
# print(b[3][1])

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(c[-1])
# print(c[4:])
# print(c[4:5])
# print(c[:5])
# print(c[::2]) # odd
# print(c[1::2]) # even

d = [1, 2, 3, 4]
e = [5, '66666', 7, False]
# print(d + e)

f = [1, 2, 3, 4]
f[-1] = 5

g = [1, 2, 3, 4]
# print(g)
# del g[1]
# g.remove(2)
# g.append(5)

h = 'Hello World!'
# print(h.lower())
# print(h.split(' '))
# print(h.startswith('Hello'))
address_book = ['미컴홍길동', '미컴김보현', '중문김도영', '컴전김남우']
for name in address_book:
    if name.startswith('미컴'):
        # print(name)
        pass

# print(h.endswith('World!'))

i = 'kimtree|hihello|abc'
# print(i.split('|'))

address_book = ['미컴과|김홍길동|010-1111-1111', '컴전|고길동|010-2222-2222']
for address in address_book:
    # print(address[:2])
    result = address.split('|')
    # print(result[0])

j = [1, 2, 3, 4]
j_animals = ['cat', 'dog', 'turtle']
j_animal_str = 'catdogturtle'
print(3 in j)
print('cat' in j_animals)

# 아래의 결과는 동일
print('og' in j_animal_str)
print(j_animal_str.find('og') != -1)
