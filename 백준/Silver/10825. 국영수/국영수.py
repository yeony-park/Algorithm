import sys

input = sys.stdin.readline

n = int(input())
s = [input().strip().split(' ') for _ in range(n)]
sorted_s = sorted(s, key=lambda s: (-int(s[1]), int(s[2]), -int(s[3]), s[0]))

print('\n'.join(s[0] for s in sorted_s))