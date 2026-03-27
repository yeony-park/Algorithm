def solution(points, routes):
    result = 0
    robot_routes = []
    # 노드 좌표 세팅
    nodes = [0]*(len(points)+1)
    for i in range(len(points)):
        nodes[i+1] = points[i]

    for i in routes:
        r = [tuple(nodes[i[0]])]
        for j in range(len(i)-1):
            stt = nodes[i[j]]
            end = nodes[i[j+1]]

            x1 = stt[0]
            y1 = stt[1]
            x2 = end[0]
            y2 = end[1]

            while x1!=x2:
                if x1 > x2:
                    x1 -= 1
                    r.append((x1,y1))
                else:
                    x1 += 1
                    r.append((x1,y1))

            while y1!=y2:        
                if y1 > y2:
                    y1 -= 1
                    r.append((x1,y1))
                else:
                    y1 +=1
                    r.append((x1,y1))

        robot_routes.append(r)

    max_t = 0
    for i in robot_routes:
        max_t = max(max_t, len(i))

    risk = 0
    for t in range(max_t+1):
        check = len(robot_routes)
        spot = {}
        for i in robot_routes:
            if t < len(i):
                if i[t] in spot:
                    spot[i[t]] += 1
                else:
                    spot[i[t]] = 1

        for k, v in spot.items():
            if v > 1:
                risk += 1

    return risk