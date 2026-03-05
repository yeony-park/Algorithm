import sys
from collections import Counter

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

def dfs(x,y):
    if x <= -1 or x >= n or y <=-1 or y >= n:
        return 0

    if graph[x][y] == 1:
        graph[x][y] = 0

        return 1 + dfs(x-1,y) + dfs(x, y-1) + dfs(x+1,y) + dfs(x,y+1)
    return 0

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(dfs(i,j))

result.sort()
print(len(result))
print("\n".join(map(str,result)))