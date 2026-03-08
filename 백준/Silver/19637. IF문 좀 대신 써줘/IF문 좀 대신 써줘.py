import sys
from bisect import bisect_left

input = sys.stdin.readline

N, M = map(int, input().split())
title = []
power = []

for _ in range(N):
    t, p = input().strip().split()
    title.append(t)
    power.append(int(p))

for _ in range(M):
    char = int(input())
    idx = bisect_left(power, char)
    print(title[idx])