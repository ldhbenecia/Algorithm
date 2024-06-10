import sys
input = sys.stdin.readline

n = int(input())
liquids = sorted(list(map(int, input().split())))

start = 0
end = n - 1
answer = abs(liquids[start] + liquids[end])
answer_start = 0
answer_end = n - 1

while start < end:
  temp = liquids[start] + liquids[end]
  
  # 0에 가장 가까운 값은 절댓값이 가장 작은 수
  # min 값을 계속 찾아서 동기화
  if abs(temp) <= answer:
    answer_start = start
    answer_end = end
    answer = abs(temp)
    
  if answer == 0:
    break
  
  if temp < answer:
    start += 1
  else:
    end -= 1
    
print(liquids[answer_start], liquids[answer_end])