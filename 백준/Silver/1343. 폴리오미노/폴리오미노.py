import sys

polio = sys.stdin.readline().strip()
answer = []
i = 0
n = len(polio)

while i < n:
    if polio[i] == '.':
        answer.append('.')
        i += 1
    else:
        j = i
        while j < n and polio[j] == 'X':
            j += 1
        
        x_len = j - i
        if x_len % 2 == 1:
            answer.clear()
            answer.append('-1')
            break

        answer.append('AAAA' * (x_len // 4) + 'BB' * ((x_len % 4)//2))
        i = j

print(''.join(answer))