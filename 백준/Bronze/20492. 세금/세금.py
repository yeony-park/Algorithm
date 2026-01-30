import sys

input = sys.stdin.readline
n = int(input())
a = int(n*(1-0.22))
b = int(n*(1-0.2*0.22))

print(a, b)