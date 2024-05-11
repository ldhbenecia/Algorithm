# 생성된 정점의 번호, 도넛 수, 막대 수, 8자 수
# 정점의 번호: 들어오는 간선 = 0, 나가는 간선 수 >= 2
# 도넛 수: 8자랑 막대 그래프 수 구해서 총에서 빼주기
# 막대 수: 들어오는 간선 1 
# 8자 수: 들어오는거 2개, 나가는거 2개
def solution(edges):
    answer = [0, 0, 0, 0]
    trunk = {}
    
    for a, b in edges: # a: 나가는 간선, b: 들어오는 간선
        if a not in trunk:
            trunk[a] = [0, 0]
        if b not in trunk:
            trunk[b] = [0, 0]
            
        trunk[a][0] += 1
        trunk[b][1] += 1
    
    for node, item in trunk.items():
        give = item[0]
        take = item[1]
        
        if give >= 2 and take == 0: # 생성한 정점
            answer[0] = node
        elif give >= 2 and take >= 2: # 8자 모양
            answer[3] += 1
        elif give == 0 and take >= 1: # 막대 모양
            answer[2] += 1
        
    # 전체 그래프 개수 == 정점에서 나가는 간선의 개수
    answer[1] = trunk[answer[0]][0] - answer[2] - answer[3]
        
    return answer 