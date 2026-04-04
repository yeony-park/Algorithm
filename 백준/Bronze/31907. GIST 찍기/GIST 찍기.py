import sys

input = sys.stdin.readline

K = int(input())

G = 'G'*K + '...'*K
IT = '.'*K + 'I'*K + '.'*K + 'T'*K
S = '..'*K + 'S'*K + '.'*K

for _ in range(K):
    print(G)

for _ in range(K):
    print(IT)

for _ in range(K):
    print(S)
