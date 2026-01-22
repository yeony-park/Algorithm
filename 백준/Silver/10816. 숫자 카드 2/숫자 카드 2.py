import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))[:n]
m = int(input())
b = list(map(int, input().split()))[:m]

count_dict = Counter(a)
for i in b:
    print(count_dict.get(i, 0), end=' ')