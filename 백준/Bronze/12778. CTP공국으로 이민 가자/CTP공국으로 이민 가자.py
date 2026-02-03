import sys

input = sys.stdin.readline
t = int(input())
trial = 0

while trial < t:
    a = []
    n, q = input().split()
    n = int(n)
    s = input().strip().split()[:n]

    for i in s:
        if q == 'C':
            i = int(ord(i))-64
            a.append(str(i))
        else:
            i = int(i)+64
            a.append(chr(i))
    print(" ".join(a))
    trial += 1