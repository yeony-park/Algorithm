import sys

input = sys.stdin.readline

N = int(input())

price = [int(input().strip()) for _ in range(N)]
price.sort(reverse=True) # 내림차순

pay = 0

for i in range(1, N+1):
    if i%3 == 0:
        continue
    else:
        pay += price[i-1]

print(pay)