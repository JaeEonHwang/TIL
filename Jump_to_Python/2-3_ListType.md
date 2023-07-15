# 2-3. 리스트 자료형
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