import sys
input = sys.stdin.readline

n = list(map(int, input().split()))
t = 0

for i in n:
    t += i**2
print(t%10)
