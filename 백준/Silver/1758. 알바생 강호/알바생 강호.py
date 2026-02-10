import sys
IN = sys.stdin.readline

N = int(IN())
tips = [int(IN()) for _ in range(N)]
tips.sort(reverse=True) # 오름차순

ans = 0

for i in range(N):
    tip = tips[i] - i
    if tip < 0:
        tip = 0
    ans += tip

print(ans)