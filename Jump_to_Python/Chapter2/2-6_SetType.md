# 2-6. 세트(집합) 자료형
* 세트 자료형의 특징
    * 중복을 허용하지 않는다.
    * 순서가 없다.
* list(), set(), tuple()은 서로 변환 가능
    ```python
    list({1,2,3}) = [1,2,3]
    ```
* 세트의 집합 계산
    ```python
    # 교집합
    S1 & S2
    S1.intersection(S2)

    # 합집합
    S1 | S2
    S1.union(S2)

    # 차집합
    S1 - S2
    S1.difference(S2)
    ```
* 세트 자료형 함수<br>
: set.add(), set.update(), set.remove()