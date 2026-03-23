import sys

input = sys.stdin.readline

n = int(input())
graph = [[False] * 26 for _ in range(26)]

for _ in range(n):
    n1, n2 = input().strip().split(' is ')
    graph[ord(n1) - ord('a')][ord(n2) - ord('a')] = True

for k in range(26):
    for i in range(26):
        for j in range(26):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

m = int(input())
for _ in range(m):
    n3, n4 = input().strip().split(' is ')
    if graph[ord(n3) - ord('a')][ord(n4) - ord('a')]:
        print('T')
    else:
        print('F')