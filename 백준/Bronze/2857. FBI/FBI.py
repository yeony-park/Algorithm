import sys
import re

input = sys.stdin.readline
fbi = []

for i in range(1,6):
    code_name = input().strip()
    if 'FBI' in code_name:
        p = re.findall(r'[^A-Z0-9-]', code_name)
        if p:
            continue
        else:
            fbi.append(str(i))

print(' '.join(fbi) if fbi else 'HE GOT AWAY!')