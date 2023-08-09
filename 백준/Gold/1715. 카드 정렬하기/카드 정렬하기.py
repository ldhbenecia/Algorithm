import heapq

n = int(input())

cardList = []
result = 0

for _ in range(n):
  card = int(input())
  heapq.heappush(cardList, card)


while len(cardList) > 1:
  previous = heapq.heappop(cardList)
  current = heapq.heappop(cardList)
  result += previous + current
  
  heapq.heappush(cardList, previous + current)

print(result)


# 오름차순 정렬 이후 앞에서부터 두 개씩 묶어서 누적합을 구하면 됨
# 구현이 도저히 생각이 안나서 구글링 했는데 우선순위 큐 방식을 활용하면 쉽게 해결 가능
'''
a = cardList[0] + cardList[1] # 30
b = a + cardList[2] # 70
c = a + b # 100

print(c)
'''