import sys

input = sys.stdin.readline

money = int(input())
MD = list(map(int, input().split()))

def BNP(money):
    stock = 0
    remain = money
    for i in range(len(MD)):
        stock += remain // MD[i]
        remain %= MD[i]
    return MD[-1] * stock + remain

def TIMING(money):
    stock = 0
    remain = money
    for i in range(len(MD)):
        if i > 2:
            if (MD[i-3] < MD[i-2]) and (MD[i-2] < MD[i-1]) and (MD[i-1] < MD[i]) and (stock > 0):
                remain += MD[i] * stock
                stock = 0
            elif (MD[i-3] > MD[i-2]) and (MD[i-2] > MD[i-1]) and (MD[i-1] > MD[i]):
                stock += remain // MD[i]
                remain %= MD[i]
    return MD[-1] * stock + remain

if BNP(money) > TIMING(money):
    print("BNP")
elif BNP(money) < TIMING(money):
    print("TIMING")
else:
    print("SAMESAME")