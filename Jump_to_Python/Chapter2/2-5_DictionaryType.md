# 2-5. 딕셔너리 자료형
* 딕셔너리에서 value 추출<br>
    ```python
    dic[key]
    # key가 없을 때 오류

    dic.get(key)
    # key가 없을 때 'None' 출력
    ```
* 딕셔너리 쌍 추가하기<br>
    ```python
    dic[key] = value
    ```
* 딕셔너리 요소 삭제하기<br>
    ```python
    del dic[key]
    ```
* 딕셔너리 관련 함수<br>
: dic.keys(), dic.values(),dic.items(), dic.clear()
    * dict_keys, dict_values, dict_items 를 리스트 형식으로 리턴하고 싶으면 list(함수)를 사용하면 된다.
* key는 고유한 값
    * 같은 key가 2개 이상 있을 경우 제일 뒤에 있는 쌍만 살아남음
        ```python
        a = {1:'a', 1:'b'}
        a
        {1:'b'}
        ```    
    * list 같이 변할 수 있는 요소는 key로 사용 불가 (value는 사용 가능)
