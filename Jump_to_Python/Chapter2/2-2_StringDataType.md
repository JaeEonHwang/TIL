# 2-2. 문자열 자료형
* 이스케이프 코드
    |코드|설명|
    |---|---|
    |\n|줄바꿈|
    |\t|탭 간격|
    |\\\\ |문자열에 \포함|
    |\\\'|문자열에 '포함|
    |\\\"|문자열에 "포함|
    |\r|캐리지 리턴(커서를 현재줄 가장 앞으로|
    |\f|폼 피드(커서 위치 그대로 두고 줄 바꿈)|
    |\v|수직탭|
    |\a|벨소리|
    |\b|백스페이스|
    |\000|널문자|
* raw string
    ```python
    print(r'\\hello\nworld\\')
    \\hello\nworld\\
    # 이스케이프 기능을 무시하고 그대로 문자열을 추가할 때, 문자열 앞에 r 추가
    ```
* formatting
    ```python
    # 요소 직접 대입
    'I have %d apples.' % 3

    # 변수 대입
    number = 3
    'I have %d apples.' % number

    # format 함수
    'I have {0} apples.'.format(3)

    # format 함수 + 변수
    number = 3
    'I have {0} apples.'.format(number)

    # 이름 대입
    'I have {number} apples.'.format(number=3)

    # f 문자열 포매팅
    number = 3
    f'I have {number} apples.'
    (f 문자열 포매팅은 표현식도 가능)

    # f 문자열 포매팅 + 딕셔너리
    {'number':3}
    f'I have {d['number']} apples.'

    # 2개 이상의 요소&변수&이름을 넣는 것도 가능
    ```
* 문자열 포맷 코드
    |코드|설명|
    |---|---|
    |%s|문자열|
    |%c|문자 1개|
    |%d|정수|
    |%f|부동소수|
    |%0|8진수|
    |%x|16진수|
    |%%|%|
* 정렬과 공백
    ```python
    # 오른쪽 정렬
    "%10s" % "hi"
    "{0:>10}".format("hi")
    f'{"hi":>10}'
    '        hi'
    
    # 왼쪽 정렬    
    "%-10sjane." % 'hi'
    "{0:<10}jane".format('hi')
    f'{"hi":<10}jane'
    'hi        jane.'
    
    # 가운데 정렬
    "{0:^10}".format("hi")
    f'{"hi":^10}'
    '    hi    '

    # 공백 채우기
    "{0:=^10}".format("hi")
    f'{"hi":=^10}'
    '====hi===='
    ```
* 소수점 표현과 공백
    ```python
    # 칸 수 설정 & 좌우 공백
    "%10.4f" % 3.42134234 
    "{0:10.4f}".format(3.42134234)
    f'{3.42134234:10.4f}'
    '    3.4213'

    # 빈칸에 0 채우기
    f'{3.42134234:010.4f}'
    '00003.4213'
    ```
* 문자열 관련 함수<br>
: count, find, index, join, upper, lower, lstrip, rstrip, strip, replace, split