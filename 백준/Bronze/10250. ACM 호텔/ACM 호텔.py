import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = str(N % H)
    if floor == '0':
        floor = str(H)
        room_num = str(N//H)
    else:
        room_num = str(N//H + 1)
    
    if len(room_num) < 2:
        room = floor + '0' + room_num
    else:
        room = floor + room_num
    print(room)
