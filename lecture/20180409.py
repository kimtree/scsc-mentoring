import random

# range(10) - iterator
i = 0
while i < 10:
    print(i)
    i += 1

for i in range(10):
    print(i)

# range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, '*', j, '=', str(i*j))

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # range(10)

# for / for string
b = [1, 2, 3, 4]
for i in b:
    print(i)

c = ['apple', 'banana', 'citron']
for i in c:
    print(i)

d = 'I am student'
for i in d:
    print(i)

# if elif else break return
condition = condition2 = condition3 = True

# Binary
if condition:
    pass
else:
    pass

# Grading
score = 77
if score > 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

if score > 90:
    grade = 'A'
else:
    if score >= 80:
        grade = 'B'
    else:
        if score >= 70:
            grade = 'C'
        else:
            grade = 'F'

# 무조건 비교 4번
if score > 90:
    grade = 'A'
if score >= 80:
    grade = 'B'
if score >= 70:
    grade = 'C'
if score < 70:
    grade = 'F'

# break / continue
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

names = ['김', '이', '박', '박']
for name in names:
    if name == '박':
        continue
    print(name)

# dictionary .keys() .values()
dict_a = {
    'name': 'Namwoo Kim',
    'student_no': '2010003970'
}
print(dict_a['name'])
print(dict_a.keys())
print(dict_a.values())

for k in dict_a.keys():
    print(k, end=' ')
    print(dict_a[k])

# list dict difference -- ordered keys
a = [1, 3, 2, 4]
b = {
    'apple': 2,
    'k1': 1,
    'k4': 4,
    'banana': 3,
}

# print(a[2])
# print(b['banana'])

# random choice
candidates = [1, 2, 3]
choice = random.choice(candidates)
# print(choice)

# list unpack
_, two, three, four, _ = [1, 2, 3, 4, 5]
print(two)
print(three)
print(four)

# None - 아무 것도 아닌 자료형
a = None  # false
if a:
    print('not none')
else:
    print('none')

#
score = [90, 80, 75, 70, 60]


# Call by reference
def change_scores(score_list):
    for i in range(len(score_list)):
        score_list[i] += 5


# Call by value
def change_score(score):
    score += 5

    return score


print(score)
change_scores(score)
print(score)

score = 10
print(score)
score = change_score(10)
print(score)