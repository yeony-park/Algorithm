import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]
lans.sort()

# 초기화
start = 1
end = max(lans)

result  = 0
while (start<=end):
    total = 0
    mid = (start + end)//2
    for x in lans:
        total += x//mid
    if total < n:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)