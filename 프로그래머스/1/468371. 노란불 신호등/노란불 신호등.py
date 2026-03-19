from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(signals):
    check = ''
    periods = []
    for G, Y, R in signals:
        periods.append(G + Y + R)

    max_try = periods[0]
    for p in periods[1:]:
        max_try = lcm(max_try, p)
    
    for i in range(len(signals)):
        G, Y, R = signals[i]
        t = G+Y+R
        q, r = divmod(max_try, t)
        txt = '0'*G + '1'*Y + '0'*R
        ch = txt*q+txt[:r]
        if check == '':
            check = ch
        else:
            ch2 = ''
            for idx in range(max_try):
                if ch[idx] == '1' and ch[idx] == check[idx]:
                    ch2 += '1'
                else:
                    ch2 += '0'
            check = ch2
    for i in range(max_try):
        if check[i] == '1':
            return i+1
    return -1