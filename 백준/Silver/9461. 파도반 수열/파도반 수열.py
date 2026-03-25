import sys

input = sys.stdin.readline

T = int(input())
n = [int(input()) for _ in range(T)]

d = [0]*(max(n)+1)

def dp(num):
    if num < 3:
        return 1
    if d[num] != 0:
        return d[num]
    else:
        d[num] = dp(num-3) + dp(num-2)
        return d[num]

for i in n:
    d[i-1] = dp(i-1)
    print(d[i-1])