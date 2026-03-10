import sys

input = sys.stdin.readline

T = int(input())

def sum_T(n):
    tn = 0
    for i in range(1,n+1):
        tn += i
    return tn

def calculate_Wn(n):
    wn = 0
    for i in range(1, n+1):
        wn += i*sum_T(i+1)
    return wn        

for _ in range(T):
    n = int(input())
    w_n = calculate_Wn(n)
    print(w_n)