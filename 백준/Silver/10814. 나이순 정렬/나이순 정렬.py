import sys

input = sys.stdin.readline

N =int(input())
members = []

for _ in range(N):
    age, name = input().strip().split()
    members.append([int(age),name])

members.sort(key=lambda x : x[0])

for age, name in members:
    print(age, name)