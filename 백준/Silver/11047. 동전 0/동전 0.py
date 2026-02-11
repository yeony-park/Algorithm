import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input().strip()) for _ in range(N)]
coins.sort(reverse=True)

cnt = 0

for c in coins:
    if K < c:
        continue
    else:
        if c == 1:
            cnt += K // c
        else:
            cnt += K // c
            K %= c

print(cnt)