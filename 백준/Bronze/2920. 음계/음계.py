import sys

input = sys.stdin.readline

music = list(map(int, input().split()))

asc = sorted(music)
des = sorted(music, reverse=True)

if music == asc:
    print("ascending")
elif music == des:
    print("descending")
else:
    print("mixed")