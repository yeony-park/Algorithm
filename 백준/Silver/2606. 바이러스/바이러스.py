import sys
input = sys.stdin.readline

cmp = int(input()) # 컴퓨터 수
pair = int(input()) # 연결된 쌍 수

graph = [[] for _ in range(cmp+1)]
visited = [False] * (cmp + 1)

for _ in range(pair):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(v):
    visited[v] = True
    cnt = 0

    for nxt in graph[v]:
        if not visited[nxt]:
            cnt += 1
            cnt += dfs(nxt)
    return cnt

print(dfs(1))