* continue: while문의 제일 처음으로 돌아가기
* 리스트 컴프리헨션
    ```python
    result = [x*y for x in range(2,10) for y in range(1,10)]

    a = [1,2,3,4]
    result = [num * 3 for num in a if num % 2 == 0]
    ```