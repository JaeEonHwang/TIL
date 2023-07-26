# 파일 읽고 쓰기
* 파일_객체 = open(파일_이름, 파일_열기_모드)
```python
# 파일 열기
f = open(folder path/"새파일.txt", 'w')
f.close()

# folder path 생략하면 프로그램을 실행한 디렉터리에 파일 생성
```
|파일열기모드|설명|
|---|---|
|r|일기모드: 파일을 읽기만 할 때 사용한다.|
|w|쓰기 모드: 파일에 내용을 쓸 때 사용한다. (파일이 이미 존재할 경우 원래 내용이 모두 사라짐)|
|a|추가 모드: 파일의 마지막에 새로운 내용을 추가할 때 사용한다.|

* 파일을 쓰기 모드(w)로 열면, 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.
* 파이썬 코드에서 파일 경로를 표시할 때는 `/` or `\\` or (r string + `\`) 사용

```python
# 파일에 내용 쓰기
f = open("folder path/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data) # 파일에 내용을 입력하는 메서드
f.close()
```

```python
# 파일 읽기 1
f = open("folder path/새파일.txt", 'r')
while True:
    line = f.readline() # 파일을 한 줄씩 읽는 메서드
    if not line: break
    print(line)
f.close()
```

```python
# 파일 읽기 2
f = open("folder path/새파일.txt", 'r')
lines = f.readlines() # 파일의 모든 줄을 읽고 각각의 줄을 요소로 가지는 리스트를 반환하는 메서드
for line in lines:
    print(line)
f.close()
```

```python
# 파일 읽기 3
f = open("folder path/새파일.txt", 'r')
data = f.read() # 파일 전체 내용을 문자열로 리턴
print(data)
f.close()
```

```python
# 파일 읽기 4
f = open("C:/doit/새파일.txt", 'r')
for line in f:  # for 이용
    print(line)
f.close()
```