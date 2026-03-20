def solution(x, n):
    answer = []
    start = x
    for i in range(n):
        answer.append(start)
        start += x
    return answer