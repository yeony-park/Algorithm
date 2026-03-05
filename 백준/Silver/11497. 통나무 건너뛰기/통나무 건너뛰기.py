import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    tmp = []
    result = []

    for i, val in enumerate(a):
        if i % 2 == 0:
            tmp.append(val)
        else:
            tmp.insert(0, val)
    
    for i in range(len(tmp)):
        diff = abs(tmp[i] - tmp[(i+1) % len(tmp)])
        result.append(diff)

    print(max(result))