# 함수
* 하나의 함수에 '위치 인자'와 '임의의 키워드 인자'가 함께 쓰일 수도 있음
    ```python
    def add_mul(choice, *args): 
    if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
         result = 0 
         for i in args: 
             result = result + i 
     elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
         result = 1 
         for i in args: 
             result = result * i 
     return result 
    ```
* 함수의 리턴 값은 항상 하나
    * return a,b일 경우: (a,b)이 반환됨
    * return a /n return b 일 경우: a가 반환되고 함수에서 빠져나옴
* return을 사용하면서 반환값이 없을 경우 함수에서 빠져나올 수 있다.
* 초깃값이 있는 매개변수는 함수 선언 단계에서 항상 제일 뒤에 와야한다.