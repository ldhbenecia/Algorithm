city = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
current_cost = price[0]
for i in range(city - 1):
    if price[i] < current_cost:
        current_cost = price[i]
    
    result += current_cost * distance[i]
        
print(result)

# 도시 4개
# [2, 3, 1] 거리
# [5, 2, 4, 1] 기름 가격
# 제일 왼쪽에서 제일 오른쪽으로 가야한다.

# 방법 1: 5 * 6 = 30
# 방법 2: 5 * 2 + 2 * 3 + 4 * 1 = 20
# 방법 3: 5 * 2 + 2 * 4 = 18

# 리터당 가격을 비교해서 가장 비싼 도시에서는 바로 그 다음 칸으로 갈 만큼의 기름만 충전해야함
# 가장 싼 도시에서는 끝까지 째면 됨