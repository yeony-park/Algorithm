import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
# N개의 도시, M개의 단방향 도로.
# 최단 거리가 K개인 도시 개수 세기
# X는 시작 노드

INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance = [-1] * (N+1)

# graph setting
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B) # 단방향

q = deque([X])
distance[X] = 0

while q:
    now = q.popleft()

    for nxt in graph[now]:
        if distance[nxt] == -1:
            distance[nxt] = distance[now] + 1
            q.append(nxt)

found = False

for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        found = True

if not found:
    print(-1)