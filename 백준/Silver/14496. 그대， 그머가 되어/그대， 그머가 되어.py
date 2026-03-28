import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [-1] * (N+1)

# graph setting
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

q = deque([a])
distance[a] = 0
dist = []

while q:
    now = q.popleft()

    for nxt in graph[now]:
        if distance[nxt] == -1:
            distance[nxt] = distance[now] + 1
            q.append(nxt)
        if nxt == b:
            dist.append(distance[nxt])
            continue

if dist:
    print(min(dist))
else:
    print(-1)