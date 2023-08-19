# 5-3 패키지
* 관련있는 모듈의 집합
## 패키지 안에 있는 함수 실행 방법
```python
import game.sound.echo
game.sound.echo.echo_test()
# echo

from game.sound.echo import echo_test
echo_test()
# echo

import game
game.sound.echo.echo_test()
# 에러, import 된 지점 아래에 있는 모듈(python 파일)이나 함수만 불러올 수 있음
# 하위 디렉터리는 참조 불가

import game.sound.echo.echo_test
# 에러, 온점을 사용해서 import 할 때 가장 마지막 항목은 반드시 모듈 혹은 패키지여야 한다.
```

## __init__.py의 용도
* 해당 디렉터리가 패키지의 일부임을 알려줌 (3.3 이후 버전에는 없어도 패키지로 인식)
* 패키지 수준에서 변수 및 함수 정의
* 패키지 내 모듈을 미리 import
    ```python
    # C:/doit/game/__init__.py
    from .sound.echo import echo_test

    # C:/doit
    import game
    game.echo_test
    # echo
    ```
* 패키지 초기화<br>
: 패키지를 처음 불러올 때 실행되어야 하는 코드를 작성할 수 있다.
    * 초기화 코드는 game 패키지의 하위 모듈의 함수를 import 할 경우에도 실행된다.
    * 초기화 코드가 한 번 실행된 후에는 다시 import를 하더라도 실행되지 않는다.
## __all__
* from 의 마지막 항목이 디렉터리인 경우, *를 사용하여 모듈을 import 하기 위해서는 __init__.py 에 __all__ 변수 설정이 필요하다
    * from 의 마지막 항목이 모듈일 경우, __all__ 과 상관없이 모든 함수를 부를 수 있다.
```python
# C:/doit.game.soune/__init__.py
__all__ = ['echo']
```
## relative 패키지
* 같은 패키지에 있는 다른 모듈/함수를 호출할 때 relative한 접근자를 사용할 수 있음

|접근자|설명|
|---|---|
|..|부모 디렉터리|
|.|현재 디렉터리|