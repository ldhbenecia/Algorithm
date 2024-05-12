def solution(picks, minerals):
    answer = 0
    
    minerals = minerals[:sum(picks)*5]
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    
    costs = []
    for mineral in minerals:
        cost = [0, 0, 0] # dia, iron, stone
        for mine in mineral:
            if mine == 'diamond':
                cost[0] += 1
                cost[1] += 5
                cost[2] += 25
            elif mine == 'iron':
                cost[0] += 1
                cost[1] += 1
                cost[2] += 5
            else:
                cost[0] += 1
                cost[1] += 1
                cost[2] += 1
        costs.append(cost)

    # 낮은 등급의 곡괭이 점수를 기준으로 내림차순 정렬
    costs.sort(key=lambda x:(-x[2],-x[1]))
    
    for cost in costs:
        for i in range(3):
            if picks[i] > 0:
                answer += cost[i]
                picks[i] -= 1
                break
    
    return answer