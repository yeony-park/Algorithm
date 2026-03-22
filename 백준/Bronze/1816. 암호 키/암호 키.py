import sys

input = sys.stdin.readline

def check_password(cp, pw):
    for i in range(2,cp):
        if pw % i == 0:
            return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    password = int(input())
    if password >= 10**6:
        answer = check_password(10**6, password)
    else:
        answer = check_password(password, password)
    print(answer)