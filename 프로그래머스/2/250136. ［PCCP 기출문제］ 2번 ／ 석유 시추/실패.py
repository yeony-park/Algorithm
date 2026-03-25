import copy
import sys

# DFS로 구현
# 초기 런타임에러는 sys.setrecursionlimit으로 해결하였으나 반복되는 재귀 및 deppcopy에 따른 시간초과 발생

sys.setrecursionlimit(300000)

def solution(land):
    answer = 0
    global n
    n = len(land)
    global m
    m = len(land[0])
    global graph
    graph = land

    for i in range(m):
        result = 0
        graph = copy.deepcopy(land)
        for j in range(n):
            result += dfs(j, i)
        answer = max(answer, result)
    return answer

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0
        return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)
    return 0
