import sys

input = sys.stdin.readline

n = int(input())
a = 0
s = 0

while s <= n:
    a += 1
    s += a

print(a-1)