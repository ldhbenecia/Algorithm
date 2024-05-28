import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    # 1. 우선순위 큐를 이용하여 (음식 시간, 음식 번호) 형태로 삽입
    queue = []
    for i in range(len(food_times)):
        heapq.heappush(queue, (food_times[i], i + 1))
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    # sum_value + (현재 음식 섭취 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((queue[0][0] - previous) * length) <= k:
        now = heapq.heappop(queue)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 최신화
        
    result = sorted(queue, key = lambda x: x[1]) # 음식 번호 기준 정렬
    return result[(k - sum_value) % length][1]

# 모든 음식을 시간을 기준으로 정렬한 후, 시간이 적게 걸리는 음식부터 제거해나간다.
# [8, 6, 4], k = 15 라고 가정하자.
# step 1.
# [(4, 3), (8, 1), (6, 2)] 위와 같은 우선순위 큐가 나온다.
# 섭취하는데 4초가 걸리는 음식이 가장 빨리 먹을 수 있는 음식이다.
# 4초가 필요하는데 1초마다 음식이 회전하므로 이 3번 음식(4초가 걸리는)을 모두 섭취하려면 12초가 걸린다.
# sum_value = 12가 되고 k는 3이 된다.
# step 2. 
# k는 3, [(8, 1), (6, 2)]이 남았다.
# 이 중에서는 6초가 더 짧게 걸린다. 
# 남은 음식의 개수 2개 * 6 = 12인데 k가 3초밖에 남지 않아서 처리할 수 없다.
# step 3.
# 다음으로 먹어야 할 음식의 번호를 찾자.
# k = 3이므로 4번째 음식을 출력한다.
# 음식 번호 순서대로 식사를 하니 (8, 1)부터 시작한다. 1번음식.
# 8 1 6 2 8 1 6 2 -> (6, 2) 답은 2