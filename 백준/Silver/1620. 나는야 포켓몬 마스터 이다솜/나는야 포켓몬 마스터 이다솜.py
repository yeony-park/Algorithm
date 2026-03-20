import sys

input = sys.stdin.readline
n, m = map(int, input().split())
poketmon = {}
poketmon_num = {}

for i in range(1,n+1):
    mon = input().strip()
    label = str(i)
    poketmon[mon] = label
    poketmon_num[label] = mon

for _ in range(m):
    q = input().strip()
    if q in poketmon.keys():
        print(poketmon[q])
    else:
        print(poketmon_num[q])