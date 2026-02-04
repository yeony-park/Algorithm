import sys

IN = sys.stdin.readline

n = int(IN())
a = 0

for _ in range(n):
    score = IN().strip()
    if score == '100':
        a += int(score)
    else:
        score = score.replace('6','9').replace('0','9')
        a += int(score)

print((2*a+n)//(2*n))