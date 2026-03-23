def solution(n):
    answer = 1
    for i in range(2,n):
        if n%i == 1:
            answer = i
            return answer