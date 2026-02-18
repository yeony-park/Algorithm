import sys

input = sys.stdin.readline

N = int(input())
cows = {}
cnt = 0

for _ in range(N):
    c, l = map(int, input().split())
    if c in cows.keys():
        if cows[c] != l:
            cnt += 1
            cows[c] = l
    else:
        cows[c] = l

print(cnt)