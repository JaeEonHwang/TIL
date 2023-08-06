# 프로그램의 입출력
## sys 모듈
### sys.argv
파이썬 파일이 실행될 때, 파일 외부에서 파일에 필요한 인자를 불러올 수 있다.
```python
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
```
python sys2.py life is too short, you need python

### sys.stdin
input()과 같은 기능, input보다 시간이 적게 걸림
```python
import sys

# 한 개의 정수를 입력 받을 때
a = int(sys.stdin.readline())

# 한 줄에 있는 여러 개의 정수를 입력 받을 때
a, b, c = list(map(int,sys.stdin.readline().split()))

# n줄에 있는 다수의 정수를 입력 받을 때
data = [sys.stdin.readline().strip() for _ in range(n)]

# 다수의 정수를 가진 n 줄을 입력 받아 2차원 리스트에 저장할 때
data = []
n = int(sys.stdin.readline())
for _ in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
```

