from itertools import combinations 

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))

# 0: 빈칸, 1: 집, 2: 치킨집
# m: 폐업시키지 않을 치킨 집

# 집, 치킨 집 저장
result = float('inf') # 치킨 거리 초기화
house, chicken = [], []

for i in range(n):
  for j in range(n):
    if city[i][j] == 1:
      house.append([i, j])
    elif city[i][j] == 2:
      chicken.append([i, j])

# 각 집의 치킨 거리를 구한다.
# 치킨 거리가 길 경우 치킨 집 폐점
# 치킨 집을 1개부터 m개 고르는 조합을 구한 후 치킨 거리를 계산
# 치킨 거리가 가장 작은 조합을 선택

for i in combinations(chicken, m): # i: 치킨집 좌표
  #print("i",i, end="")
  chicken_distance = 0 # 조합 하나 당 도시의 치킨 거리
  for r1, c1 in house: # (r1, c1)집 좌표
    distance = float('inf') # 집마다 치킨거리 무한으로 초기화
    for r2, c2 in i: # 치킨집 좌표에 해당하는 r2, c2
      distance = min(distance, abs(r1-r2) + abs(c1-c2)) # 치킨 거리 최솟값
    chicken_distance += distance # 조합 하나당 치킨 거리
  result = min(result, chicken_distance) # 최솟값 찾기
print(result)
    