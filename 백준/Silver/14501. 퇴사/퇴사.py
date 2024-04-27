n = int(input())
consulting_list = [list(map(int, input().split())) for _ in range(n)]

price = 0
def earn(day, money):
  global price
  price = max(price, money)

  if day >= n:
    return

  # 만약 오늘 날짜 + 상담 걸리는 기간이 n보다 작을 경우 상담 가능
  if day + consulting_list[day][0] <= n:
    earn(day + consulting_list[day][0], money + consulting_list[day][1]) # 상담 하기
    earn(day + 1, money)
  else:
    earn(day + 1, money)
  return

earn(0, 0)
print(price)