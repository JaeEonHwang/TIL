# 2-1. 숫자형

* 4.24E9 = 4.24e9 = $4.24 * 10^9$
* 0b*** = 2진수, 0o*** = 8진수, 0x*** = 16진수 (다른 진수는 직접 함수로 만들어서 사용해야함)
```python
# 업데이트 해야함
```
* N진수인 수 abc를 10진수로 바꾸는 법
```python
print(int(abc,N))
```
* 나눗셈
```python
a//b = 몫
a%b = 나머지
divmod(a,b) = (몫, 나머지)
```
* 소수점
```python
round(a,b) = 반올림 # 실수 a를 소수 b자리 수까지 보이게 반올림한
# 소수부분이 2진수 근삿값으로 변환된 후 반올림 계산이 되어서 정확하게 일치하지 않을 수 있음
ex) print(round(1.45,1)) = 1.4

import math

math.ceil(a) = 소수점 올림
math.floor(a) = 소수점 내림 # math.floor(-3.4) = -4
math.trunc(a) = 소수점 버림 # math.trunc(-3.4) = -3

# math.xx 함수들은 특정 소수 자릿수를 지정해서 올리거나 내릴 수 없음. 무조건 정수로 표현
```