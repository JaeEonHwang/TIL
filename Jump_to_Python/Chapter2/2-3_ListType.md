# 2-3. 리스트 자료형
* list 관련 함수
    * del, append, sort, reverse, index, insert, remove, pop, count, extend
* list의 append(), extend(), insert() 차이점
```python
# append()
리스트의 마지막에 인자로 전달된 아이템을 추가
list = [2,9,3]
a = [1,4,5]
list.append(a) = [2,9,3,[1,4,5]]

# extend()
리스트/튜플의 인자를 리스트에 추가
list = [2,9,3]
a = [1,4,5] or (1,4,5)
list.append(a) = [2,9,3,1,4,5]

# insert()
특정 인덱스에 요소 넣기
list = [2,9,3]
a = [1]
list.insert(0,a) = [1,2,9,3]
```
* list의 del, remove(), pop()의 차이점
```python
# del list[]
특정 인덱스의 요소 빼기
list = [1,2,3]
del list[1]
list = [1,3]

# remove()
리스트에서 첫번째로 나오는 요소를 삭제
list = [1,2,3,1,2,3]
list.remove(2)
list = [1,3,1,2,3]

# pop()
리스트의 제일 마지막 요소를 리턴하고 그 요소는 리스트에서 제거
list = [1,2,3]
list.pop()
3
list = [1,2]

# pop(n)
리스트에서 n 인덱스에 있는 요소를 리턴하고 그 요소는 리스트에서 제거
list = [1,2,3]
list.pop(1)
2
list[1,3]
```
* 리스트 복사
    ```python
    b = a[:]
    # a가 변해도 b는 변하지 않음
    ```