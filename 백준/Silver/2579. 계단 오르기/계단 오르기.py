import sys

input = sys.stdin.readline
n = int(input())

steps = [0] + [int(input()) for _ in range(n)]
score = 0
d = [0] * (n+1)

# 초기화
if n >=1 :
    d[1] = steps[1]
if n >=2 :
    d[2] = steps[1] + steps[2]
if n >=3:
    d[3] = max(steps[1] + steps[3], steps[2] + steps[3])

for i in range(4,n+1):
    d[i] = max(d[i-3] + steps[i-1] + steps[i],
               d[i-2] + steps[i])

print(d[n])