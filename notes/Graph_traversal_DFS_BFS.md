# ![Tag](https://img.shields.io/badge/Tag-Graph%20Traversal-2ea44f) 그래프 탐색 알고리즘 : DFS / BFS

## 정의

* **탐색(Search)**: 많은 데이터 중에서 원하는 데이터를 찾는 과정
* 대표적인 그래프 탐색 알고리즘이 **DFS / BFS**
* 그래프뿐 아니라 **트리, 2차원 격자(Grid)** 문제에서도 매우 자주 등장

---

# ![Tag](https://img.shields.io/badge/Tag-Data%20Structure-2ea44f) 기본 자료구조: 스택 / 큐

## 스택 (Stack)

* **FILO(First In Last Out)**
* 입구와 출구가 동일 (박스 쌓기처럼 “위에 쌓고 위에서 꺼냄”)

```python
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
```

* `append`, `pop` 시간복잡도: **O(1)**

## 큐 (Queue)

* **FIFO(First In First Out)**
* 입구/출구가 모두 뚫린 구조 (대기열처럼 “먼저 온 게 먼저 나감”)
* 파이썬은 보통 `deque` 사용

```python
from collections import deque

q = deque()
q.append(5)
q.append(2)
q.popleft()
```

* `append`, `popleft` 시간복잡도: **O(1)**

---

# ![Tag](https://img.shields.io/badge/Tag-Recursion-2ea44f) 재귀 함수 (Recursion)

## 개념

* 자기 자신을 다시 호출하는 함수
* 호출이 누적되며 **스택 프레임**에 쌓이는 구조 → “스택처럼 동작”으로 이해 가능

## 유의 사항

* 파이썬은 재귀 깊이가 너무 깊으면 오류 발생

  * `RecursionError: maximum recursion depth exceeded`
* 재귀 사용 시 **종료 조건**은 필수 (없으면 무한 호출)

---

# ![Tag](https://img.shields.io/badge/Tag-DFS-2ea44f) DFS (Depth-First Search)

## 정의

* **깊이 우선 탐색**
* 그래프에서 **깊은 부분을 우선적으로** 탐색
* 구현 방식

  * **재귀(Recursive)** 또는 **스택(Stack)** 기반

## 동작 방식

1. 시작 노드를 방문 처리 후 진행
2. 현재 노드의 인접 노드 중 **아직 방문하지 않은 노드**가 있으면 그쪽으로 이동
3. 더 이상 갈 곳이 없으면 **되돌아감(backtrack)**
4. 위 과정을 반복

## 언제 유리한가

* **연결 요소(컴포넌트) 개수 세기**
* 2차원 격자에서 “붙어있는 영역” 탐색 (상/하/좌/우)
* 경로를 깊게 파고들며 조건을 만족하는지 확인하는 유형(백트래킹 포함)

## 재귀 DFS 예시 코드

```python
def dfs(graph, v, visited):
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(graph, nxt, visited)
```

---

# ![Tag](https://img.shields.io/badge/Tag-BFS-2ea44f) BFS (Breadth-First Search)

## 정의

* **너비 우선 탐색**
* 시작점에서 **가까운 노드부터** 레벨 순서로 탐색
* 구현 방식

  * **큐(Queue, deque)** 기반

## 동작 방식

1. 시작 노드를 큐에 넣고 방문 처리
2. 큐에서 하나 꺼내며(`popleft`) 인접 노드를 확인
3. 방문하지 않은 인접 노드를 큐에 넣고 방문 처리
4. 큐가 빌 때까지 반복

## 언제 유리한가

* **최단거리(최소 이동 횟수)** 문제에서 거의 정석

  * 격자 미로에서 “최단 칸 수”, “최소 이동” 류
* 동일한 비용(가중치 없는 그래프)에서 최단거리 보장

## BFS 예시 코드

```python
from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
```

---

# ![Tag](https://img.shields.io/badge/Tag-Grid-2ea44f) 2차원 격자(Grid)에서의 포인트

## 방향 벡터 템플릿

* 상/하/좌/우 이동을 벡터로 통일하면 구현이 깔끔해짐

```python
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
```

## 범위 체크

* 격자 문제는 매번 범위 체크가 핵심
* 예: `0 <= nx < n`, `0 <= ny < m`

---

# 시간 복잡도 관점

## 그래프(인접 리스트) 기준

* DFS / BFS 모두: **O(V + E)**

  * V: 정점 수, E: 간선 수
* 격자 N×M 기준

  * 정점 ~ `NM`, 간선 ~ 상하좌우 연결 → 전체 **O(NM)** 수준으로 보는 게 일반적

---

# 정리: DFS vs BFS 선택 기준

* **깊게 파고들며 영역/연결을 전부 방문** → DFS가 직관적일 때 많음
* **최단거리/최소 이동 횟수** → BFS가 정석 (가중치 없을 때)

---

## More details

[![Notion](https://img.shields.io/badge/Notion-Study%20Note-808080?logo=notion\&logoColor=000000\&labelColor=FFD700)](https://daily-archduke-be2.notion.site/DFS-BFS-3025e249d44e80c091b6ff0d8deaeab8?source=copy_link)

## References

[![YouTube](https://img.shields.io/badge/YouTube-%EC%9D%B4%EC%BD%94%ED%85%8C%20%EA%B0%95%EC%9D%98-808080?logo=youtube\&logoColor=FFFFFF\&labelColor=FF0000)](https://youtu.be/7C9RgOcvkvo?si=vRbR7av_9OizqoVa)
