import sys

input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()

a = 0
for i in range(N):
    a = max(a, ropes[i]*(N-i))

print(a)