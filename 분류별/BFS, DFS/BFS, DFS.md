# DFS
* 사용 자료구조: `stack`
* process
  * start node > stack, visited
  * stack 최상단 노드에 not visited node > stack, visited
  * 반복
* code 1(재귀 구조)
  ```python
    def DFS(start, visited):
        visited[start] = 1
        for w in graph[start]:
            if not visited[start]:
                visited = DFS(w, visited)
        return visited
  ```
* code 2(stack)
  ```python
  from collections import deque
  
  def DFS(start):
    qu = deque()
    qu.append(start)
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
      
    while qu:
      v = qu.pop()
        if not visited[v]:
          visited[v] = 1
          for w in graph[v]:
            qu.append(w)
  ```
  
# BFS
* 사용 자료구조: `queue`
* process
  * start node > queue, visited
  * queue에서 node 꺼내 인접 노드 중 not visited 모두 > queue, visited
  * 반복
* code
  ```python
  from collections import deque
      
  def BFS(start):
      qu = deque()
      qu.append(start)
      visited = [0 for _ in range(N+1)]
      visited[start] = 1
      
      while qu:
        v = qu.pop()
        for w in graph[v]:
          if not visited[w]:
            visited[w] = 1
            qu.append(w)
   ```