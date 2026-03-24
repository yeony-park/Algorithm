def solution(n):
    answer = [i for i in str(n)]
    answer.sort(reverse=True)
    answer = int("".join(answer))
    return answer