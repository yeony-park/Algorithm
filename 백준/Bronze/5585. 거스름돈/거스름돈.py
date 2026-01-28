import sys
input = sys.stdin.readline

n = 1000 - int(input())
coins = [500,100,50,10,5,1]
cnt = 0

for c in coins:
    cnt += n // c
    n %= c

print(cnt)
