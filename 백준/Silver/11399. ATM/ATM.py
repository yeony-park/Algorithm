import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

total = 0
total_sum = 0

for i in sorted(h):
    total += i
    total_sum += total
print(total_sum)