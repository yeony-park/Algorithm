# [Silver I] 단지번호붙이기 - 2667 

[문제 링크](https://www.acmicpc.net/problem/2667) 

### 성능 요약

메모리: 34936 KB, 시간: 60 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프, 플러드 필

### 제출 일자

2026년 3월 5일 18:29:42

### 문제 설명

<p><그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png" style="height:192px; width:409px"></p>

### 입력 

 <p>첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.</p>

### 출력 

 <p>첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.</p>

---
### ✅ Solve log

#### 접근 아이디어
* 2차원 배열에서 `1`인 칸을 발견하면 DFS로 연결된 영역 전체를 탐색
* DFS 탐색 시 방문한 칸을 `0`으로 덮어써서 재방문 방지
* DFS가 반환하는 값에 자기 자신(`1`)을 더하면 한 덩어리의 집 개수가 합산됨
* for문 순회 중 DFS 호출 시 재귀가 완전히 끝난 뒤 다음 인덱스로 넘어가므로 이미 방문한 덩어리는 `0`으로 소멸되어 중복 카운트가 발생하지 않는다

### 복잡도

| 구분 | 복잡도 |
|------|--------|
| 시간 | O(n²) — 모든 칸을 한 번씩 방문 |
| 공간 | O(n²) — 재귀 스택 최대 깊이 |

#### 아쉬운 점 / 개선할 사안

* 처음엔 라벨링 방식으로 접근했었다
  ```python
  import sys
  from collections import Counter
  
  input = sys.stdin.readline
  sys.setrecursionlimit(10**6)
  
  n = int(input())
  graph = [list(map(int, input().strip())) for _ in range(n)]
  
  label = 2
  
  def dfs(x,y,label):
      if x <= -1 or x >= n or y <=-1 or y >= n:
          return
  
      if graph[x][y] == 1:
          graph[x][y] = label
  
          dfs(x-1,y, label)
          dfs(x, y-1, label)
          dfs(x+1,y, label)
          dfs(x,y+1, label)
  
  for i in range(n):
      for j in range(n):
          if graph[i][j] == 1:
              dfs(i,j,label)
              label += 1
  
  flat = [v for row in graph for v in row if v >= 2]
  counter = Counter(flat)
  
  print(len(counter))
  for lab, cnt in sorted(counter.items()):
    print(cnt)
  ```
* DFS 반환값으로 집 개수를 직접 합산하는 방식이 더 간결하다고 판단하여 최종코드로 제출함
* `global label` 없이 label을 인자로 넘기는 방식도 있으나, 애초에 라벨링이 불필요한 문제였음!
