#### 1. 아래와 같은 피라미드 모양을 출력하기 위해 아래와 같이 코드를 작성하였다. 빈칸에 들어갈 코드를 쓰시오.
(조교의 피라미드 예제를 거의 그대로 사용함)
```
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
```

```python
layers = 5
i = 1

while i <= layers:
    j = 0
    while j < 2 * ( [[[ 빈칸 ]]] ):
        print(' ', end='')
        j += 1
        
    k = 1
    while k < (2 * i):
        print('*', end=' ')
        k += 1

    print()
    i += 1
```

#### 2. 아래 같은 코드가 있다. 이 때 a의 값은 어떤 값이 될 수 있는지 서술하시오.
```python
import random
a = random.randint(1, 10)
```

#### 3. 아래의 결과를 예측하시오.
(1)
```python
iteration = 0
while True:
    print(iteration)
    if iteration > 3:
        break
   
    iteration += 1
```

(2) list 형태로 예측 예) [9, 8, 7]
```python
sample_list = [1, 2, 3, 4, 5, 6]

print(sample_list[::2])
print(sample_list[2:-2])
```

(3) 
```python
for c in 'Hello World!':
    if c == 'o':
        print('a', end='')
```

(4) 
```python
data_list = ['컴전|홍길동', '중문|탕웨이', '미컴|손석희']

for value in data_list:
    data = value.split('|')
    print(data[1])
```


(5) 
```python
sample_dict = {
    'apple': 1,
    'banana': 2,
    'melon': 33,
    'grape': 91
}

try:
    print(sample_dict['orange'])
    sample_dict['melon'] = 99
except:
    print(sample_dict['melon'])
```

(6)
```python
sample_list = [1, 2, 3, 4]

sample_list[3] = 3
sample_list.append(3)

print(sample_list)
```

(7)
```python
sample_list = [1, 2, 3, 4, 5]

for sample in sample_list:
    if sample % 2 == 1:
        continue
    print(sample)
```

(8)
```python
cond1 = 21 % 2 == 0

cond2 = (cond1 and True) or True

if not cond1:
    print('X', end='')
else:
    print('O', end='')

if cond2:
    if cond1:
        print('X', end='')
    elif cond2:
        print('O', end='')
    else:
        print('N', end='')

    if cond2:
        print('X', end='')
    else:
        print('O', end='')

if not cond1 and cond2:
    print('O')
```


#### 4. 2단부터 9단까지 구구단을 출력하려고 한다. 아래의 소스 코드의 빈칸을 채우시오.
```python
for dan in range( [[[ 빈칸 ]]] ):
    start_num = 1
    max_num = 9
    # 1단부터 9단까지 반복문
    while ( [[[ 빈칸 ]]] ):
        print(str(dan) + '*' + str(start_num) + '=' + str(dan * start_num))
        start_num += 1
```

#### 5. 함수 설명에 맞는 빈칸을 채우시오.
```python
# 덧셈 함수
def add(a, b):
    [[[ 빈칸 ]]]

# 뺄셈 함수
def sub(a, b):
    [[[ 빈칸 ]]]

# 곱셈 함수
def mul(a, b):
    [[[ 빈칸 ]]]

# 나눗셈 함수
def div(a, b):
    [[[ 빈칸 ]]]
```

#### 6. 아래의 결과를 예측하시오.
```python
a = 15

def sample_func(a):
    a += 10

    return a

print(a)
sample_func(a)
print(a)
```

#### 7. 아래의 결과를 출력하기 위해 다음 빈칸을 채우시오.
```python
He said, "I can't believe you let him borrow your car." 
```
```python
print(" [[[빈칸]]] ")
```

#### 8. 다음 결과를 예측하시오.
```python
>>> 2 + int('2') 

>>> '2'  + '2'

>>> 'Hello' == 'HELLO'

>>> not True

>>> False not
```

#### 9. 다음의 에러를 수정하는 방법을 적으시오.
(1)
```python
>>> print 'adsf' + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects 
```
(2)
```python
# a.py 파일내용

function_a();
def function_a():
    print('asdf')

$ python a.py
Traceback (most recent call last):
  File "a.py", line 1, in <module>
      function_a();
NameError: name 'function_a' is not defined
```
(3)
```python
>>> random.randint(1,10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'random' is not defined
```

#### 10. 아래의 결과를 출력하기 위해서 다음 빈칸을 채우시오.
```python
162 793 414 896 460 272 255 761 804 316 
Maximum number is 896
```
```python
import random

num = []
for i in range(10):
    n = random.randint(1, 1000)
    num.append(n)

for i in num:
    print(i, end=' ')
print()

compare = 0
for i in num:
    if [[[ 빈칸 ]]]:
        [[[ 빈칸 ]]]

print('Maximum number is ' + str(compare))
```
