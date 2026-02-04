import sys

IN = sys.stdin.readline

a, d, k = map(int, IN().split())

# n = (k - a)/d + 1

t_n = 1
t_k = 0
while -1000000 < t_k < 1000000:
    t_k = a + d*(t_n-1)
    t_n += 1
    if t_k == k:
        t_n = 0
        break
    else:
        continue 

if t_n > 0:
    print('X')
else:
    print(int((k - a)//d + 1))