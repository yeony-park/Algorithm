import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

times = str(A*B*C)
cnt = [0]*10

for i in times:
    cnt[int(i)] += 1

for c in cnt:
    print(c)