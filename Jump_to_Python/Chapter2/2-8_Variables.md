# 2-8. 변수
* 변수 복사하기
    ```python
    from copy import copy
    b = copy(a)
    
    # a가 변해도 b는 변하지 않음
    ```
* 리스트, 튜플로 변수 만들기도 가능
    ```python
    a, b = [1,2]
    ```
* 간단하게 두 변수 바꾸기
    ```python
    a, b = b, a
    ```