# 프로그램의 입출력
## sys 모듈
파이썬 파일이 실행될 때, 파일 외부에서 파일에 필요한 인자를 불러올 수 있다.
```python
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
```
python sys2.py life is too short, you need python

