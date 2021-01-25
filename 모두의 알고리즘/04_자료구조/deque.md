# deque
### 1. deque개념
스택이나 큐처럼 한방향 삽입 삭제가 아니라 양방향 삽입삭제가 가능한 자료구조

### 2. collections.deque 활용
#### 1) 데이터 추가(append), 연장(extend), 삽입(insert)
```python
from collections import deque

deque.append(x)     # 맨 뒤(오른쪽) 삽입
deque.appendleft(x) # 맨 앞(왼쪽) 삽입

deque.extend(['a', 'b'])     # 맨 뒤 연장
deque.extendleft(['c', 'd']) # 맨 앞 연장

deque.insert(i, x)  # i번째에 x삽입
```
#### 2) 데이터 반환(pop)
```python
deque.pop()         # 맨 오른쪽 제거하고 return
deque.popleft()     # 맨 왼쪽 제거하고 return
```
#### 3) 데이터 삭제(remove, clear)
```python
deque.remove('a')
deque.clear()
```
#### 4) 데이터 회전 및 반전
```python
deque.reverse()   # 순서 반대로
deque.rotate(i)   # i칸 오른쪽으로 회전
```


