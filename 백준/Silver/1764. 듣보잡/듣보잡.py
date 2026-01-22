import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = set(input().strip() for i in range(n))
see = set(input().strip() for i in range(m))
not_l_s = set(listen & see)

print(len(not_l_s))
[print(i) for i in sorted(not_l_s)]
