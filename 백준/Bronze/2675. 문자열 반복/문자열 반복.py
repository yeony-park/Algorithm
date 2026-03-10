import sys

input = sys.stdin.readline

T = int(input())

def get_P(r, s):
    p = ''
    for i in s:
        p += i*r
    return p

for _ in range(T):
    R, S = input().split()
    R=int(R)
    print(get_P(R, S))