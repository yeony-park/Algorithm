def solution(s):
    n = len(s)
    mid = n//2
    if n % 2 == 0:
        answer = s[mid-1:mid+1]
    else:
        answer = s[mid]
    return answer