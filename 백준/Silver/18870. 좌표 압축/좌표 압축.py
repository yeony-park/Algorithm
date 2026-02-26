import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))[:n]
result = []

sorted_unq = sorted(set(num))
r = {v : i for i, v in enumerate(sorted_unq)}
print(*[r[x] for x in num], sep='\n')