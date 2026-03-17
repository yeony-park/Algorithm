import sys

input = sys.stdin.readline

n = int(input())
d = [0]*(n+1)

d[1] = 1
if n >=2 :
    d[2] = 2

def tile(num):
    if d[num] != 0:
        return d[num]
    d[num] = tile(num-1) + tile(num-2)
    return d[num]

print(tile(n)%10007)