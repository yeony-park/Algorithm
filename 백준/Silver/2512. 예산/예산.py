import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
requests.sort()

budget = int(input())

def total_cost(cap):
    return sum(min(r, cap) for r in requests)

start = 0
end = max(requests)
answer = 0
total_r = sum(requests)

if budget > total_r: # 초기 체크용
    answer = max(requests)
else:
    while (start <= end):
        cap = (start + end) // 2
        total_budget = total_cost(cap)

        if total_budget <= budget:
            answer = cap
            start = cap + 1
        else:
            end = cap - 1

print(answer)