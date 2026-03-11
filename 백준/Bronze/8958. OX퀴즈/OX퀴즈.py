import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = 0
    t = 0
    case = input().strip()
    
    for c in case:
        if c == 'O':
            s += 1
            t += s
        else:
            s = 0
    print(t)