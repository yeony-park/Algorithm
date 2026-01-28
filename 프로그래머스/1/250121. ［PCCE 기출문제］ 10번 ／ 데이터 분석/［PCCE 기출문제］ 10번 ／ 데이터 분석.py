def solution(data, ext, val_ext, sort_by):
    answer=[]
    ext_code = {"code" : 0,
               "date": 1,
               "maximum": 2,
               "remain": 3}
    answer = [row for row in data if row[ext_code[ext]] < val_ext]
    answer.sort(key=lambda x:x[ext_code[sort_by]], reverse=False)        
    return answer