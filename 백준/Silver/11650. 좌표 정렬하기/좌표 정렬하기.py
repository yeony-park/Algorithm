import sys

input = sys.stdin.readline

n = int(input())

pos = [list(map(int, input().split())) for _ in range(n)]
pos.sort(key=lambda pos : (pos[0], pos[1]))
print('\n'.join(f'{p[0]} {p[1]}' for p in pos))