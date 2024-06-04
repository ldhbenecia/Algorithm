n = int(input())
liquids = list(map(int, input().split()))

start = 0
end = len(liquids) - 1
answer = abs(liquids[start] + liquids[end])

ans_start = start
ans_end = end
while start < end:
  temp = liquids[start] + liquids[end]
  
  # 절댓값이 가장 작은게 0에 가까운 수
  if abs(temp) <= answer:
    ans_start = start
    ans_end = end
    answer = abs(temp)
    
    if answer == 0:
      break
    
  if temp < 0:
    start += 1
  else:
    end -= 1
    
print(liquids[ans_start], liquids[ans_end])