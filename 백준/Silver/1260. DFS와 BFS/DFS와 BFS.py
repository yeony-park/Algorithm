import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)


for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1, N + 1):
    graph[i].sort()

def dfs(v):
    visited_dfs[v] = True
    print(v, end= ' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True

    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

dfs(V)
print()
bfs(V)
print()
