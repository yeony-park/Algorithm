def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        a1 = bin(arr1[i])[2:].zfill(n)
        a2 = bin(arr2[i])[2:].zfill(n)
        r = ''
        for j in range(n):
            if a1[j] == '1' or a2[j] == '1':
                r += '#'
            else:
                r += ' '
        result.append(r)
    return result