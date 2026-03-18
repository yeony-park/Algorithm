def solution(bandage, health, attacks):
    t, x, y = bandage
    h = health
    a = attacks
    
    max_t = attacks[-1][0]
    success = 0 #스킬 연속 성공 카운팅
    idx = 0
    
    for i in range(1, max_t+1):
        # i가 현재 시간임
        if idx < len(attacks) and i == attacks[idx][0]:
            h -= attacks[idx][1]
            success = 0
            idx += 1
            if h <= 0:
                return -1
        # 공격을 안 받는 타이밍
        else:
            h += x
            success += 1
            if h >= health:
                h = health
            if success == t:
                success = 0
                h += y
                if h > health:
                    h = health
        
    return h