import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
num_total = 0
num = 0

for  i in range(1, n+1):
    for j in str(i):
        num += int(j)

    if i%num == 0:
        num_total += 1
    
    num = 0

print(num_total)