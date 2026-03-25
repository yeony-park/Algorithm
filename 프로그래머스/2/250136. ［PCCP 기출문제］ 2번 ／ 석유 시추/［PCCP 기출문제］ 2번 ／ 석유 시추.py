from collections import deque
import copy
import sys

sys.setrecursionlimit(300000)

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[-1]*m for _ in range(n)]
    oil_size = {}
    oil_id = 0

    # 1. 전체 덩어리 BFS로 id 부여해서 크기 저장
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == -1:
                queue = deque([(i,j)])
                visited[i][j] = oil_id
                size = 0
                while queue:
                    x, y = queue.popleft()
                    size += 1
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x+dx, y+dy
                        if 0 <=nx<n and 0<=ny<m and land[nx][ny]==1 and visited[nx][ny]==-1:
                            visited[nx][ny] = oil_id
                            queue.append((nx,ny))
                oil_size[oil_id] = size
                oil_id += 1
    
    # 2. 각 열마다 지나는 덩어리 id 합
    answer = 0
    for j in range(m):
        seen = set()
        for i in range(n):
            if visited[i][j] != -1:
                seen.add(visited[i][j])
        answer = max(answer, sum(oil_size[id] for id in seen))
    return answer