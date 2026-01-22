import sys
input = sys.stdin.readline

def palindrome():
    txt = str(input().strip())
    if txt == '0':
        return False
    if txt[::] == txt[::-1]:
        return print('yes')
    else:
        return print('no')

while True:
    if palindrome() == False:
        break