import sys

input = sys.stdin.readline

n = int(input())
words = set(input().strip() for _ in range(n))

words = sorted(words, key = lambda x: (len(x), x))

for w in words:
    print(w)