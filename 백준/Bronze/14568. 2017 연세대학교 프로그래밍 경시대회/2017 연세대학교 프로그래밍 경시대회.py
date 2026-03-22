import sys

input = sys.stdin.readline

N = int(input())
answer = 0

for a in range(1,N):
    for b in range(1,N):
        c = N-a-b
        if a%2 == 0:
            if c>0 and (c >= b+ 2):
                answer += 1
print(answer)