def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])

    k = -300000
    for route in routes:
        if route[0] > k:
            answer += 1
            k = route[1]
        
    return answer