def get_min(t:str):
    h, m = t.split(':')
    total = int(h)*60 + int(m)
    return total

def get_time(t:int):
    h = plus_zero(str(t//60))
    m = plus_zero(str(t%60))
    time = f"{h}:{m}"
    return time

def plus_zero(t):
    if len(t) < 2:
        t = '0'+t
    return t

def solution(video_len, pos, op_start, op_end, commands):
    pos_ = get_min(pos)
    op_start_ = get_min(op_start)
    op_end_ = get_min(op_end)
    video_len_ = get_min(video_len)

    def skip_openning(p):
        if op_start_ <= p <= op_end_:
            return op_end_
        else:
            return p
    
    for c in commands:
        pos_ = skip_openning(pos_)
        if c == 'prev':
            if pos_ < 10:
                pos_ = 0
            else:
                pos_ -= 10
        else:
            pos_ += 10
            if video_len_ - pos_ < 0:
                pos_ = video_len_

    pos_ = skip_openning(pos_)
    if pos_ > video_len_:
        pos_ = video_len_            
    answer = get_time(pos_)
    return answer