n, c = map(int, input().split())
home = sorted([int(input()) for _ in range(n)])

start = 1 # 거리 시작점
end = home[-1] - home[0] # 거리 끝점(집 좌표 중 가장 큰 값)

answer = 0
while start <= end:
  mid = (start + end) // 2
  count = 1 # 제일 첫 값은 무조건 설치
  current = home[0] # 현재 집 위치
  
  # 현재 mid 값으로 공유기 설치
  for i in range(1, n):
    if home[i] >= current + mid:
      count += 1
      current = home[i]
  
  if count < c:
    end = mid - 1
  else:
    start = mid + 1
    answer = mid
    
print(answer)
