import sys

input = sys.stdin.readline

N, X = map(int, input().split())

nums = list(map(int,input().split()))

print(" ".join([str(n) for n in nums if n < X]))